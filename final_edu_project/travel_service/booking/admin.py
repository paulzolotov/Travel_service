from django.contrib import admin
from .models import Direction, DateRoute, TimeTrip

# Register your models here.


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретном Направлении маршрута."""

    list_display = ("name", "slug", "start_point", "end_point", "travel_time")


@admin.register(DateRoute)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной Дате, определенного Направления."""

    list_display = ("data_route", "slug", "direction_name", "amount_trips")


@admin.register(TimeTrip)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной Дате, определенного Направления."""

    list_display = ("departure_time", "date_of_the_trip", "carrier", "number_of_seats")
