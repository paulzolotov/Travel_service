from datetime import datetime, timedelta, date
import time

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import get_object_or_404


# Create your models here.
class BookingInfoMixin(models.Model):
    """Класс Mixin, для повторяющихся полей, от которого затем наследуются классы с моделями"""

    is_active = models.BooleanField(default=True, verbose_name="Is it active?")

    class Meta:
        abstract = True


class Direction(BookingInfoMixin):
    """Класс для создания модели - Направление поездки"""

    slug = models.SlugField(max_length=70, verbose_name="Short Name")
    name = models.CharField(max_length=70, verbose_name="Direction Name")
    start_point = models.CharField(max_length=40, verbose_name="Where does the route start?")
    end_point = models.CharField(max_length=40, verbose_name="Where does the route end?")
    list_of_stops = models.CharField(default="Rest.1, Rest.2", max_length=200,
                                     verbose_name="Enter stops separated by commas.(For example: Rest.1, Rest.2)")
    travel_time = models.IntegerField(default=0, validators=[MinValueValidator(1)], verbose_name="Travel time in minutes")

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
            list_of_stops="default",
        )
        return direction.pk

    def format_travel_time(self):
        """Функция, предназначенная для форматирования времени пути т.е минуты переводим в часы и минуты"""

        return time.strftime("%H:%M", time.gmtime(self.travel_time * 60))

    def min_price(self):
        """Функция, предназначенная для подсчета минимальной цены от всех предложенных во все дни
         т.е по всем имеющимся записям маршрутов"""
        dateroutes_from_direction = self.dateroute_set.filter(is_active=True).all()
        price_list = []
        for dateroute in dateroutes_from_direction:
            timetrips_from_dateroute = dateroute.timetrip_set.filter(direction=self.id).all()
            for timetrip in timetrips_from_dateroute:
                price_list.append(timetrip.price)
        if price_list:
            min_price = min(price_list)
        else:
            min_price = 0
        return min_price


class DateRoute(BookingInfoMixin):
    """Класс для создания модели - Дата поездки"""

    date_route = models.DateField(
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

        return f"{self.date_route}"


class TimeTrip(models.Model):
    """Класс для создания модели - Время начала поездки"""

    departure_time = models.TimeField(verbose_name="Departure time")
    date_of_the_trip = models.ForeignKey(DateRoute, verbose_name="Travel date", on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, default=Direction.get_default_direction_pk,
                                  verbose_name="Travel direction", on_delete=models.CASCADE, null=True)
    car = models.CharField(default='Mercedes-Benz Sprinter', max_length=80, verbose_name="Car Name")
    auto_number = models.CharField(default='1234AB-7', max_length=10, verbose_name="Auto Number")
    carrier_phone = PhoneNumberField()
    number_of_seats = models.IntegerField(default=20, validators=[MinValueValidator(1)], verbose_name="Number of seats")
    price = models.IntegerField(default=0, validators=[MinValueValidator(1)], verbose_name="Price per seats")

    class Meta:
        verbose_name = "TimeTrip"
        verbose_name_plural = "TimeTrips"

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.departure_time}"

    def number_of_reserved_places_in_trip(self):
        """Функция для подсчета количества зарезервированных мест в данной поездке"""

        trip_from_time = self.trip_set.all()
        sum_places = 0
        if trip_from_time:
            sum_places = sum(
                list(map(lambda trip: trip.number_of_reserved_places, trip_from_time))
            )
        return f"{sum_places}"

    def number_of_free_places_in_trip(self):
        """Функция, предназначенная для подсчета количества свободных мест
        на определенное дату и время"""

        count_free_places = self.number_of_seats - int(self.number_of_reserved_places_in_trip())
        return f"{count_free_places}"

    def arrival_time_calculation(self):
        """Функция, предназначенная для подсчета времени прибытия"""

        minutes = self.direction.travel_time
        result = datetime.combine(date.today(), self.departure_time) + timedelta(minutes=int(minutes))
        return result.time()


class Trip(models.Model):
    """Класс для создания модели - Информация о поездке"""

    CHOICES = (
        ('1', 'Ост. 1'),
        ('2', 'Ост. 2'),
        ('3', 'Ост. 3'),
        ('4', 'Ост. 4'),
        ('5', 'Ост. 5'),
    )

    username = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User name", on_delete=models.CASCADE)
    departure_time = models.ForeignKey(TimeTrip, verbose_name="Departure time", on_delete=models.CASCADE)
    date_of_the_trip = models.ForeignKey(DateRoute, verbose_name="Trip date", on_delete=models.CASCADE, null=True)
    number_of_reserved_places = models.IntegerField(default=1, validators=[MinValueValidator(1)],
                                                    verbose_name="Reserved places")
    landing_place = models.CharField(max_length=300, choices=CHOICES, verbose_name="Landing place")
    user_comment = models.CharField(max_length=200, verbose_name="User Comment", null=True, blank=True)

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.username}"

    def get_price(self):
        """Функция, достающая информацию о цене за одно место в поездке"""

        price = self.departure_time.price
        return price

    def get_full_price(self):
        """Функция, подсчитывающая полную цену за поездку с учетом количества забронированных мест"""

        price = self.get_price() * self.number_of_reserved_places
        return price

    def number_of_free_places_in_trip(self):
        """Функция, достающая информацию о количестве свободных мест в поездке"""

        seats = self.departure_time.number_of_free_places_in_trip()
        return seats

    # def clean(self):
    #
    #     free_seats = self.number_of_free_places_in_trip()
    #     if self.number_of_reserved_places > free_seats:
    #         raise ValidationError(
    #                     'Осталось свободных мест: %(value)s',
    #                     params={'value': free_seats},
    #                 )

    def get_list_stops(self):
        """Надо связать list_of_stops в Direction с landing_place """

        ...
