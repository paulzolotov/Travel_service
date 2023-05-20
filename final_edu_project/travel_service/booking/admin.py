import csv
import datetime

from django import forms
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import DateRoute, Direction, Log, TimeTrip, Trip


# Register your models here.
class ContactForm(forms.ModelForm):
    """Класс для установки виджета для поля 'номер телефона'"""

    class Meta:
        widgets = {
            "carrier_phone": PhoneNumberPrefixWidget(
                initial="BY",
                country_choices=[("BY", "375"), ("RU", "7"), ("UA", "380")],
            ),
        }


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретном Направлении маршрута."""

    list_display = (
        "name",
        "is_active",
        "slug",
        "start_point",
        "end_point",
        "travel_time",
        "list_of_stops",
    )
    actions = ("make_inactive", "make_active")

    @admin.action(description="Перевести в неактивное состояние")
    def make_inactive(self, request: HttpRequest, queryset) -> None:
        """Функция для перевода в строке 'action' в состояние 'inactive'"""

        queryset.update(is_active=False)

    @admin.action(description="Перевести в активное состояние")
    def make_active(self, request: HttpRequest, queryset) -> None:
        """Функция для перевода в строке 'action' в состояние 'active'"""

        queryset.update(is_active=True)


@admin.register(DateRoute)
class DateRouteAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной Дате, определенного Направления."""

    filter_horizontal = [
        "direction_name"
    ]  # применили для наглядной демонстрации используемых маршрутов в день
    list_display = (
        "date_route",
        "view_time_trips_link",
        "is_active",
    )
    sortable_by = ("date_route",)
    list_filter = ("date_route", "is_active")
    actions = ("make_inactive",)

    @admin.display(description="time_trips")
    def view_time_trips_link(self, obj):
        """Функция для подсчета количества временных отправлений в данной день, а также генерации ссылки
        на эти временные отправления"""

        count = obj.timetrip_set.count()
        url = (
            reverse("admin:booking_timetrip_changelist")
            + "?"
            + urlencode({"date_of_the_trip_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} TimeTrips</a>', url, count)

    @admin.action(description="Перевести в неактивное состояние")
    def make_inactive(self, request: HttpRequest, queryset) -> None:
        """Функция для проверки даты с текущей и если данная дата уже прошла, то переводим выбранные неподходящие даты
        в строке 'action' в состояние 'inactive'"""

        # today = datetime.datetime(2023, 4, 7).date()  # необходимо для тестирования
        today = datetime.datetime.now().date()
        print(queryset)
        for obj in queryset:
            date = obj.date_route
            if date < today:
                queryset.filter(date_route=date).update(is_active=False)


@admin.register(TimeTrip)
class TimeTripAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретных временных отметках, в
    которые возможно отправление."""

    form = ContactForm
    list_display = (
        "departure_time",
        "date_of_the_trip",
        "direction",
        "is_active",
        "view_trips_link",
        "number_of_seats",
        "number_of_reserved_places_in_trip",
        "number_of_free_places_in_trip",
        "show_pretty_price",
        "car",
        "auto_number",
        "carrier_phone",
    )
    sortable_by = ("departure_time", "date_of_the_trip", "direction")
    list_filter = ("departure_time", "date_of_the_trip", "direction")
    actions = ("export_to_csv",)

    @admin.display(description="custom price")
    def show_pretty_price(self, obj) -> str:
        """Функция для отображения кастомной записи для 'цены за место' (В данном случае добавили знак $)"""

        return f"{obj.price} BYN"

    @admin.display(description="trips")
    def view_trips_link(self, obj):
        """Функция для подсчета количества совершенных бронирований данной поездки, а также генерации ссылки
        на эти брони"""

        count = obj.trip_set.count()
        url = (
            reverse("admin:booking_trip_changelist")
            + "?"
            + urlencode({"departure_time_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Trips</a>', url, count)

    @admin.action(description="Export to CSV")
    def export_to_csv(self, request: HttpRequest, queryset) -> HttpResponse:
        """Функция для выгрузки данных в виде логов в формате CSV"""
        opts = self.model._meta
        # Создаем экземпляр HttpResponse, включающий кастомный text/csv-тип контента, чтобы сообщить браузеру,
        # что ответ должен обрабатываться как файл CSV. Также добавляется заголовок Content-Disposition, указывающий,
        # что HTTP-ответ содержит вложенный файл.
        response = HttpResponse(content_type="text/csv")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={opts.verbose_name_plural}.csv"
        writer = csv.writer(response)
        # Записываем строку заголовка, включая имена полей.
        fields = opts.get_fields()  # Возвращает кортеж полей
        writer.writerow(
            [field.verbose_name for field in fields if hasattr(field, "verbose_name")]
        )
        # Записываем строку для каждого объекта
        for obj in queryset:
            data_row = [
                getattr(obj, field.name) for field in fields if field.name != "trip"
            ]
            writer.writerow(data_row)
        return response


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной поездке в определенное время."""

    list_display = (
        "username",
        "date_of_the_trip",
        "departure_time",
        "number_of_reserved_places",
        "landing_place",
        "user_comment",
        "get_price",
        "get_full_price",
        "get_list_stops",
    )
    sortable_by = ()


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о Логах."""

    list_display = ("log_datetime", "log_path", "log_user")
    readonly_fields = (
        "log_datetime",
        "log_path",
        "log_user",
    )  # Делаем так, чтобы логи нельзя было редактировать.
    search_fields = ("log_user",)
