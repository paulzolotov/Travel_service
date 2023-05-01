import time
from datetime import date, datetime, timedelta
from typing import Any

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
    start_point = models.CharField(
        max_length=40, verbose_name="Where does the route start?"
    )
    end_point = models.CharField(
        max_length=40, verbose_name="Where does the route end?"
    )
    list_of_stops = models.CharField(
        default="Rest.1, Rest.2",
        max_length=200,
        verbose_name="Enter stops separated by commas.(For example: Rest.1, Rest.2)",
    )
    travel_time = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1)],
        verbose_name="Travel time in minutes",
    )

    class Meta:
        verbose_name = "Direction"
        verbose_name_plural = "Directions"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"

    @classmethod
    def get_default_direction_pk(cls) -> Any:
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

    def format_travel_time(self) -> str:
        """Функция, предназначенная для форматирования времени пути т.е минуты переводим в часы и минуты"""

        return time.strftime("%H:%M", time.gmtime(self.travel_time * 60))

    def min_price(self) -> int:
        """Функция, предназначенная для подсчета минимальной цены от всех предложенных во все дни
        т.е по всем имеющимся записям маршрутов"""

        dateroutes_from_direction = self.dateroute_set.filter(is_active=True).all()
        price_list = []
        for dateroute in dateroutes_from_direction:
            timetrips_from_dateroute = dateroute.timetrip_set.filter(
                direction=self.id
            ).all()
            for timetrip in timetrips_from_dateroute:
                price_list.append(timetrip.price)
        if price_list:
            min_price = min(price_list)
        else:
            min_price = 0
        return min_price


class DateRoute(BookingInfoMixin):
    """Класс для создания модели - Дата поездки"""

    date_route = models.DateField(verbose_name="Date of trip", auto_now_add=False)
    direction_name = models.ManyToManyField(
        Direction,
        verbose_name="Direction Name",
    )

    class Meta:
        verbose_name = "DateRoute"
        verbose_name_plural = "DateRoutes"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.date_route}"


class TimeTrip(models.Model):
    """Класс для создания модели - Время начала поездки"""

    departure_time = models.TimeField(verbose_name="Departure time")
    date_of_the_trip = models.ForeignKey(
        DateRoute, verbose_name="Travel date", on_delete=models.CASCADE
    )
    direction = models.ForeignKey(
        Direction,
        default=Direction.get_default_direction_pk,
        verbose_name="Travel direction",
        on_delete=models.CASCADE,
        null=True,
    )
    car = models.CharField(
        default="Mercedes-Benz Sprinter", max_length=80, verbose_name="Car Name"
    )
    auto_number = models.CharField(
        default="1234AB-7", max_length=10, verbose_name="Auto Number"
    )
    carrier_phone = PhoneNumberField()
    number_of_seats = models.IntegerField(
        default=20, validators=[MinValueValidator(1)], verbose_name="Number of seats"
    )
    price = models.IntegerField(
        default=0, validators=[MinValueValidator(1)], verbose_name="Price per seats"
    )

    class Meta:
        verbose_name = "TimeTrip"
        verbose_name_plural = "TimeTrips"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.departure_time}"

    def number_of_reserved_places_in_trip(self) -> str:
        """Функция для подсчета количества зарезервированных мест в данной поездке"""

        trip_from_time = self.trip_set.all()
        sum_places = 0
        if trip_from_time:
            sum_places = sum(
                list(map(lambda trip: trip.number_of_reserved_places, trip_from_time))
            )
        return f"{sum_places}"

    def number_of_free_places_in_trip(self) -> str:
        """Функция, предназначенная для подсчета количества свободных мест
        на определенное дату и время"""

        count_free_places = self.number_of_seats - int(
            self.number_of_reserved_places_in_trip()
        )
        return f"{count_free_places}"

    def arrival_time_calculation(self) -> time:
        """Функция, предназначенная для подсчета времени прибытия"""

        minutes = self.direction.travel_time
        result = datetime.combine(date.today(), self.departure_time) + timedelta(
            minutes=int(minutes)
        )
        return result.time()


class Trip(models.Model):
    """Класс для создания модели - Информация о поездке"""

    CHOICES = (
        ("1", "Ост. 1"),
        ("2", "Ост. 2"),
        ("3", "Ост. 3"),
        ("4", "Ост. 4"),
        ("5", "Ост. 5"),
    )

    username = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="User name", on_delete=models.CASCADE
    )
    departure_time = models.ForeignKey(
        TimeTrip, verbose_name="Departure time", on_delete=models.CASCADE
    )
    date_of_the_trip = models.ForeignKey(
        DateRoute, verbose_name="Trip date", on_delete=models.CASCADE, null=True
    )
    number_of_reserved_places = models.IntegerField(
        default=1, validators=[MinValueValidator(1)], verbose_name="Reserved places"
    )
    landing_place = models.CharField(
        max_length=300, choices=CHOICES, verbose_name="Landing place"
    )
    user_comment = models.CharField(
        max_length=200, verbose_name="User Comment", null=True, blank=True
    )
    user_trip_ticket = models.FileField(upload_to='booking/', null=True, blank=True)

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.username}"

    def get_price(self) -> int:
        """Функция, достающая информацию о цене за одно место в поездке"""

        price = self.departure_time.price
        return price

    def get_full_price(self) -> int:
        """Функция, подсчитывающая полную цену за поездку с учетом количества забронированных мест"""

        price = self.get_price() * self.number_of_reserved_places
        return price

    def number_of_free_places_in_trip(self) -> int:
        """Функция, достающая информацию о количестве свободных мест в поездке"""

        return self.departure_time.number_of_free_places_in_trip()

    def car_info_in_trip(self) -> dict:
        """Функция, достающая информацию о перевозчике в данной поездке"""

        car_info = {
            "name": self.departure_time.car,
            "auto_number": self.departure_time.auto_number,
            "carrier_phone": self.departure_time.carrier_phone,
        }
        return car_info

    def arrival_time_calculation(self) -> str:
        """Функция, достающая информацию о перевозчике в данной поездке"""

        return self.departure_time.arrival_time_calculation()

    def get_direction(self) -> str:
        """Функция, достающая информацию о направлении данной поездке"""

        return self.departure_time.direction.name

    def get_list_stops(self):
        """Надо связать list_of_stops в Direction с landing_place"""

        return (
            self.departure_time.direction.list_of_stops
        )  # НЕ знаю как передать полученный результат в
        # CHOICES поля landing_place модели Trip
