import datetime
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import TripModelForm
from .models import Direction, Trip

# Create your views here.


def index(request: HttpRequest) -> HttpRequest:
    """Функция предназначена для перехода к странице со списком направлений"""

    directions = Direction.objects.filter(is_active=True).all()
    today = str(
        datetime.datetime(2023, 4, 6).date()
    )  # указываем определенный день, чтобы записи в бд
    # не создавать каждый раз
    # today = datetime.datetime.now().date()
    return render(
        request,
        "booking/index.html",
        context={"directions": directions, "today": today},
    )


def get_daytime_trip(
    request: HttpRequest, direction_slug: str, date_route: datetime
) -> HttpRequest:
    """Функция предназначена для перехода к странице со списком дней в которые имеются поездки по данному направлению.
    При выборе определенной даты, высвечиваются все возможные поездки, по умолчанию при переходе на данную страницу
    выбирается текущий день
    """

    # Получили список всех дат по которым возможна бронь поездки
    direction = get_object_or_404(Direction, slug=direction_slug)
    date_routes = direction.dateroute_set.filter(
        is_active=True
    ).all()  # dateroute в dateroute_set взяли из модели
    # Получили список всех поездок сортированных по времени (с утра до вечера)
    day = get_object_or_404(date_routes, date_route=date_route)
    # timetrip в timetrip_set взяли из модели
    trip_times = (
        day.timetrip_set.filter(direction=direction).order_by("departure_time").all()
    )
    return render(
        request,
        "booking/daytime_trip.html",
        context={
            "direction": direction,
            "direction_slug": direction_slug,
            "date_routes": date_routes,
            "trip_times": trip_times,
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
                "trip_id": self.kwargs["trip_id"],
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
        trip_id = self.kwargs["trip_id"]
        trip_times = (
            day.timetrip_set.filter(direction=direction)
            .order_by("departure_time")
            .all()
        )
        time = get_object_or_404(trip_times, id=trip_id)
        return direction, day, time

    def form_valid(self, form: Any) -> HttpRequest:
        """Функция для проверки валидности"""

        direction, day, time = self.get_path_params()

        form.instance.username = self.request.user
        form.instance.date_of_the_trip = day
        form.instance.departure_time = time

        # Необходимо для валидации поля number_of_reserved_places модели Trip. Достаем значение о количестве свободных
        # мест в поездке
        direction, day, time = self.get_path_params()
        number_of_seats = int(form.instance.number_of_reserved_places)
        number_of_free_seats = int(time.number_of_free_places_in_trip())

        if number_of_seats > number_of_free_seats:
            form.add_error(
                "number_of_reserved_places",
                f"Свободных мест осталось {number_of_free_seats}",
            )
            return super().form_invalid(form)

        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


def booking_success(
    request: HttpRequest, direction_slug: str, date_route: datetime, trip_id: int
) -> HttpRequest:
    """Функция, предназначенная для перехода к template после успешного бронирования поездки"""

    context = {}
    return render(request, "booking/booking_success.html", context=context)


def account(request: HttpRequest) -> HttpRequest:
    """Функция предназначена для перехода к странице с контактной информацией"""

    user_trips = None
    if request.user.is_authenticated:
        user_trips = Trip.objects.filter(username=request.user)

    return render(request, "booking/account.html", context={"user_trips": user_trips})


def trip_remove_in_account(request: HttpRequest, trip_id: int) -> HttpRequest:
    """Функция предназначена для удаления поездки из всех поездок пользователя"""

    trip = Trip.objects.get(username=request.user, id=trip_id)
    trip.delete()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def contacts(request: HttpRequest) -> HttpRequest:
    """Функция предназначена для перехода к странице с контактной информацией"""

    return render(request, "booking/contacts.html")
