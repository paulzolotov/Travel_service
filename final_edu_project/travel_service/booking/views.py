from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from .models import Direction, DateRoute, TimeTrip, Trip

# Create your views here.


def index(request: HttpRequest):
    """Функция предназначена для перехода к странице со списком направлений"""

    directions = Direction.objects.filter(is_active=True).all()
    today = '2023_04_05'  # сделать по сегодняшнему дню
    return render(request, "booking/index.html", context={"directions": directions, "today": today})


def get_direction(request: HttpRequest, direction_slug, date_route):
    """Функция предназначена для перехода к странице со списком дней в которые имеются поездки по данному направлению.
    При выборе определенной даты, высвечиваются все возможные поездки, по умолчанию при переходе на данную страницу
    выбирается текущий день
    """

    # Получили список всех дат по которым возможна бронь поездки
    direction = get_object_or_404(Direction, slug=direction_slug)
    date_routes = direction.dateroute_set.filter(is_active=True).all()  # dateroute в dateroute_set взяли из модели
    # Получили список всех поездок сортированных по времени (с утра до вечера)
    day = get_object_or_404(date_routes, slug=date_route)
    trip_times = day.timetrip_set.all()  # timetrip в timetrip_set взяли из модели
    return render(request, "booking/direction.html", context={"direction_slug": direction_slug, "date_routes": date_routes, "trip_times": trip_times})


def contacts(request: HttpRequest):
    """Функция предназначена для перехода к странице с контактной информацией"""

    return render(request, "booking/contacts.html")
