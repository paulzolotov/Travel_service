from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from .models import Direction, DateRoute, TimeTrip, Trip
import datetime
# Create your views here.


def index(request: HttpRequest):
    """Функция предназначена для перехода к странице со списком направлений"""

    directions = Direction.objects.filter(is_active=True).all()
    today = str(datetime.datetime(2023, 4, 6).date())  # указываем определенный день, чтобы записи в .replace('-', '_')
    # бд не создавать каждый раз
    # today = datetime.datetime.now().date()
    return render(request, "booking/index.html", context={"directions": directions, "today": today})


def get_daytime_trip(request: HttpRequest, direction_slug, date_route):
    """Функция предназначена для перехода к странице со списком дней в которые имеются поездки по данному направлению.
    При выборе определенной даты, высвечиваются все возможные поездки, по умолчанию при переходе на данную страницу
    выбирается текущий день
    """

    # Получили список всех дат по которым возможна бронь поездки
    direction = get_object_or_404(Direction, slug=direction_slug)
    date_routes = direction.dateroute_set.filter(is_active=True).all()  # dateroute в dateroute_set взяли из модели
    # Получили список всех поездок сортированных по времени (с утра до вечера)
    day = get_object_or_404(date_routes, date_route=date_route)
    trip_times = day.timetrip_set.all()  # timetrip в timetrip_set взяли из модели
    return render(request, "booking/daytime_trip.html", context={"direction": direction,
                                                                 "direction_slug": direction_slug,
                                                                 "date_routes": date_routes, "trip_times": trip_times})


def booking_trip(request: HttpRequest, direction_slug, date_route, trip_id):
    """Функция предназначена для перехода к странице для бронирования места в данной поездке
    """

    direction = get_object_or_404(Direction, slug=direction_slug)
    date_routes = direction.dateroute_set.filter(is_active=True).all()  # dateroute в dateroute_set взяли из модели
    # Получили список всех поездок сортированных по времени (с утра до вечера)
    day = get_object_or_404(date_routes, date_route=date_route)
    trip_times = day.timetrip_set.all()  # timetrip в timetrip_set взяли из модели
    time = get_object_or_404(trip_times, id=trip_id)
    records = time.trip_set.all()
    print(records)
    for rec in records:
        print(rec.date_of_the_trip)
    return render(request, "booking/trip.html")


def contacts(request: HttpRequest):
    """Функция предназначена для перехода к странице с контактной информацией"""

    return render(request, "booking/contacts.html")
