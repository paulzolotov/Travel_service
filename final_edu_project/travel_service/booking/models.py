import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class BookingInfoMixin(models.Model):
    """Класс Mixin, для повторяющихся полей, от которого затем наследуются классы с моделями"""

    slug = models.SlugField(max_length=70, verbose_name="Short Name")
    is_active = models.BooleanField(default=True, verbose_name="Is it active?")

    class Meta:
        abstract = True


class Direction(BookingInfoMixin):
    """Класс для создания модели - Направление поездки"""

    name = models.CharField(max_length=70, verbose_name="Direction Name")
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
            is_active=False,
        )
        return direction.pk

    def min_price(self):
        """Функция, предназначенная для подсчета минимальной цены от всех предложенных во все дни
         т.е по всем имеющимся записям маршрутов"""
        min_price = self.dateroute_set.all()[0].timetrip_set.all()
        return min_price


class DateRoute(BookingInfoMixin):
    """Класс для создания модели - Дата поездки"""

    data_route = models.DateField(
        verbose_name="Date of trip", auto_now_add=False
    )
    direction_name = models.ManyToManyField(
        Direction,
        verbose_name="Direction Name",
    )

    class Meta:
        verbose_name = "DateRoute"
        verbose_name_plural = "DateRoutes"

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.data_route}"

    def min_price(self):
        """Функция, предназначенная для подсчета минимальной цены в определенный день"""
        min_price = self.dateroute_set.all()[0].timetrip_set.all()
        return min_price

    def max_price(self):
        """Функция, предназначенная для подсчета максимальной цены в определенный день"""
        ...


class TimeTrip(models.Model):
    """Класс для создания модели - Время начала поездки"""

    departure_time = models.TimeField(verbose_name="Departure time")
    date_of_the_trip = models.ForeignKey(DateRoute, verbose_name="Travel date", on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, default=Direction.get_default_direction_pk,
                                  verbose_name="Travel direction", on_delete=models.CASCADE, null=True)
    car = models.CharField(default='Mercedes-Benz Sprinter', max_length=80, verbose_name="Car Name")
    auto_number = models.CharField(default='1234AB-7', max_length=10, verbose_name="Auto Number")
    carrier_phone = PhoneNumberField(default='+375441111111')
    number_of_seats = models.IntegerField(default=0, verbose_name="Number of seats")
    price = models.IntegerField(default=0, verbose_name="Price per seats")

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


class Trip(models.Model):
    """Класс для создания модели - Информация о поездке"""

    user_phone = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User phone", on_delete=models.CASCADE)
    departure_time = models.ForeignKey(TimeTrip, verbose_name="Departure time", on_delete=models.CASCADE)
    number_of_reserved_places = models.IntegerField(default=0, verbose_name="Reserved places")
    landing_place = models.CharField(max_length=70, verbose_name="Landing place")

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.user_phone}"

