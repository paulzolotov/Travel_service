import datetime
import os
from typing import Any

import pdfkit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.files.base import File
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import CreateView

from .forms import TripModelForm
from .models import Direction, Trip
from .tasks import send_tripticket_task
from .utils import decorator_log


# Create your views here.
@decorator_log
def index(request: HttpRequest) -> HttpRequest:
    """Функция предназначена для перехода к странице со списком направлений"""

    directions = Direction.objects.filter(is_active=True).all()
    today = str(
        datetime.datetime(2023, 4, 6).date()
    )  # for debug - указываем определенный день, чтобы записи в бд
    # не создавать каждый раз
    # today = datetime.datetime.now().date()
    return render(
        request,
        "booking/index.html",
        context={"directions": directions, "today": today},
    )


@decorator_log
def get_daytime_trip(
    request: HttpRequest, direction_slug: str, date_route: datetime
) -> HttpRequest:
    """Функция предназначена для перехода к странице со списком дней в которые имеются поездки по данному направлению.
    При выборе определенной даты, высвечиваются все возможные поездки, по умолчанию при переходе на данную страницу
    выбирается текущий день
    """

    # Получили список всех дат по которым возможна бронь поездки
    direction = get_object_or_404(Direction, slug=direction_slug)
    date_routes = (
        direction.dateroute_set.filter(is_active=True).order_by("date_route").all()
    )  # dateroute в dateroute_set взяли из модели
    # Получили список всех поездок сортированных по времени (с утра до вечера)
    day = get_object_or_404(date_routes, date_route=date_route)
    # timetrip в timetrip_set взяли из модели
    trip_times_all = (
        day.timetrip_set.filter(direction=direction).order_by("departure_time").all()
    )
    trip_times_active = (
        day.timetrip_set.filter(direction=direction, is_active=True)
        .order_by("departure_time")
        .all()
    )
    return render(
        request,
        "booking/daytime_trip.html",
        context={
            "direction": direction,
            "direction_slug": direction_slug,
            "date_routes": date_routes,
            "trip_times_all": trip_times_all,
            "trip_times_active": trip_times_active,
        },
    )


class TripCreateView(LoginRequiredMixin, CreateView):
    """Класс для бронирования поездки. LoginRequiredMixin - ограничивает доступ не аутентифицированным пользователям"""

    model = Trip
    form_class = TripModelForm  # либо form_class либо fields
    template_name = "booking/trip.html"

    def get_context_data(self, **kwargs) -> dict:
        """Функция для передачи context в template"""

        context = super().get_context_data(**kwargs)
        direction, day, time = self.get_path_params()
        context["direction"] = direction
        context["day"] = day
        context["time"] = time
        return context

    def get_success_url(self) -> str:
        """URL, на который будет произведено перенаправление"""

        return reverse(
            "booking:trip-success",
            kwargs={
                "direction_slug": self.kwargs["direction_slug"],
                "date_route": self.kwargs["date_route"],
                "timetrip_id": self.kwargs["timetrip_id"],
            },
        )

    def get_path_params(self) -> Any:
        """Функция, предназначенная для получения записей, по параметрам пути"""

        direction_slug = self.kwargs["direction_slug"]
        direction = get_object_or_404(Direction, slug=direction_slug)
        date_routes = direction.dateroute_set.filter(
            is_active=True
        ).all()  # dateroute в dateroute_set взяли из модели
        # Получили список всех поездок сортированных по времени (с утра до вечера)
        date_route = self.kwargs["date_route"]
        day = get_object_or_404(date_routes, date_route=date_route)
        # timetrip в timetrip_set взяли из модели
        timetrip_id = self.kwargs["timetrip_id"]
        trip_times = (
            day.timetrip_set.filter(direction=direction)
            .order_by("departure_time")
            .all()
        )
        time = get_object_or_404(trip_times, id=timetrip_id)

        return direction, day, time

    def form_valid(self, form: Any) -> HttpResponseRedirect:
        """Функция для проверки валидности"""

        direction, day, time = self.get_path_params()

        # Проверка того, имеет ли пользователь запись на данную поездку.
        # Идея такая: 1 пользователь - 1 заказ на данную поездку
        trip = time.trip_set.filter(username=self.request.user)
        if trip:
            return HttpResponseRedirect(
                reverse(
                    "booking:trip-impossible",
                    kwargs={
                        "direction_slug": self.kwargs["direction_slug"],
                        "date_route": self.kwargs["date_route"],
                        "timetrip_id": self.kwargs["timetrip_id"],
                    },
                )
            )

        form.instance.username = self.request.user
        form.instance.date_of_the_trip = day
        form.instance.departure_time = time

        # Необходимо для валидации поля number_of_reserved_places модели Trip. Достаем значение о количестве свободных
        # мест в поездке
        number_of_seats = form.instance.number_of_reserved_places
        number_of_free_seats = time.number_of_free_places_in_trip()

        if number_of_seats > number_of_free_seats:
            form.add_error(
                "number_of_reserved_places",
                f"Свободных мест осталось {number_of_free_seats}",
            )
            return super().form_invalid(form)

        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


@decorator_log
def booking_success(
    request: HttpRequest, direction_slug: str, date_route: datetime, timetrip_id: int
) -> HttpRequest:
    """Функция, предназначенная для перехода к template после успешного бронирования поездки"""

    trip = Trip.objects.get(username=request.user, departure_time=timetrip_id)

    # Генерация html шаблона билета
    template = get_template("ticket.html")
    context = {"trip": trip}
    ticket_template = template.render(context)
    ticket_name = (
        f"{trip.username}_{trip.get_direction()}_{trip.date_of_the_trip}_{trip.departure_time}_"
        f"{datetime.datetime.now()}.pdf"
    )
    # Конвертирование html шаблона в pdf файл
    css_path = os.path.join(os.path.dirname(__file__), "static/css/style_booking.css")
    pdfkit.from_string(ticket_template, f"media/booking/{ticket_name}", css=css_path)

    # Задача в celery
    send_tripticket_task.delay(
        request.user.email, ticket_name, serializers.serialize("json", [trip])
    )

    context = {"ticket_template": ticket_template}
    return render(request, "booking/booking_success.html", context=context)


@decorator_log
def booking_impossible(
    request: HttpRequest, direction_slug: str, date_route: datetime, timetrip_id: int
) -> HttpRequest:
    """Функция, предназначенная для перехода к template в случае, если пользователь бронировал уже данную поездку"""

    return render(request, "booking/booking_impossible.html")


@login_required(login_url="users:login", redirect_field_name="next")
@decorator_log
def trips_history(request):
    """Функция предназначена для перехода к странице с информацией о поездках, которые уже прошли и попали
    в историю поездок пользователя

    Идея такая, что как только день время поездки проходит, т.е с помощью celery становится неактивным, то поездки
    переходит в историю поездок пользователя.
    """

    user_inactive_trips = [
        x
        for x in Trip.objects.filter(username=request.user)
        if not x.departure_time.is_active
    ]

    return render(
        request,
        "booking/user_trip_history.html",
        context={"user_trips": user_inactive_trips},
    )


@login_required(login_url="users:login", redirect_field_name="next")
@decorator_log
def account(request: HttpRequest) -> HttpRequest:
    """Функция предназначена для перехода к странице с контактной информацией и отображением все активных
    поездок пользователя"""

    user_trips = [
        x
        for x in Trip.objects.filter(username=request.user)
        if x.departure_time.is_active
    ]

    return render(request, "booking/account.html", context={"user_trips": user_trips})


@decorator_log
def trip_remove_in_account(request: HttpRequest, trip_id: int) -> HttpResponseRedirect:
    """Функция предназначена для удаления поездки из всех поездок пользователя"""

    trip = Trip.objects.get(username=request.user, id=trip_id)
    trip.delete()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@decorator_log
def contacts(request: HttpRequest) -> HttpRequest:
    """Функция предназначена для перехода к странице с контактной информацией"""

    return render(request, "booking/contacts.html")
