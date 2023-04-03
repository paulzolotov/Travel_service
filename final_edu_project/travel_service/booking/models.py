import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.


class Direction(models.Model):
    """Класс для создания модели - Направление поездки"""

    name = models.CharField(max_length=70, verbose_name="Direction Name")
    slug = models.SlugField(max_length=70, verbose_name="Short Name")
    start_point = models.CharField(max_length=40, verbose_name="Where does the route start?")
    end_point = models.CharField(max_length=40, verbose_name="Where does the route end?")
    travel_time = models.IntegerField(default=0, verbose_name="Travel time in minutes")

    class Meta:
        verbose_name = "Direction"
        verbose_name_plural = "Directions"

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"

    @classmethod
    def get_default_direction_pk(cls):
        """Необходим для значений по default"""

        direction, created = cls.objects.get_or_create(
            name="Default",
            slug="default",
            start_point="default",
            end_point="default",
            travel_time=0,
        )
        return direction.pk

    def max_min_price(self):
        """Функция, предназначенная для подсчета максимальной и минимальной цены от всех предложенных во все дни
         т.е по всем имеющимся записям маршрутов"""
        ...


class DateRoute(models.Model):
    """Класс для создания модели - Дата поездки"""

    data_route = models.DateField(
        verbose_name="Date of trip", auto_now_add=False
    )
    slug = models.SlugField(max_length=30, verbose_name="Short DateName")
    direction_name = models.ForeignKey(
        Direction,
        verbose_name="Direction Name",
        on_delete=models.SET_DEFAULT,
        default=Direction.get_default_direction_pk,
        null=True,
    )
    amount_trips = models.IntegerField(
        default=0, verbose_name="Trips Amount In Date"
    )

    class Meta:
        verbose_name = "DateRoute"
        verbose_name_plural = "DateRoutes"

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.data_route}"

    def max_min_price(self):
        """Функция, предназначенная для подсчета максимальной и минимальной цены в определенный день"""
        ...


class TimeTrip(models.Model):
    """Класс для создания модели - Время начала поездки"""

    departure_time = models.TimeField(verbose_name="Departure time")
    date_of_the_trip = models.ForeignKey(DateRoute, verbose_name="Travel date", on_delete=models.CASCADE)
    carrier = models.CharField(max_length=80, verbose_name="Carrier Name")
    number_of_seats = models.IntegerField(default=0, verbose_name="Number of seats")

    class Meta:
        verbose_name = "TimeTrip"
        verbose_name_plural = "TimeTrips"

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.departure_time}"

    def number_of_reserved_places(self):
        """Функция, предназначенная для подсчета количества забронированных мест пользователями
        на определенное дату и время"""
        ...

    def arrival_time_calculation(self):
        """Функция, предназначенная для подсчета времени прибытия"""
        ...
