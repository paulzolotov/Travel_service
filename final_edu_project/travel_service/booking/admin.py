import datetime

from django.contrib import admin
from .models import Direction, DateRoute, TimeTrip, Trip
from django import forms
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.http import HttpResponse
import csv


# Register your models here.
class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'carrier_phone': PhoneNumberPrefixWidget(initial='BY',
                                                     country_choices=[
                                                         ("BY", "375"),
                                                         ("RU", "7"),
                                                         ("UA", "380")
                                                     ],
                                                     ),
        }


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретном Направлении маршрута."""

    list_display = ("name", "is_active", "slug", "start_point", "end_point", "travel_time")
    actions = (
        "make_inactive",
        "make_active"
    )

    @admin.action(description="Switch to inactive state")
    def make_inactive(self, request, queryset):
        """Функция для перевода в строке 'action' в состояние 'inactive'"""

        queryset.update(is_active=False)

    @admin.action(description="Switch to active state")
    def make_active(self, request, queryset):
        """Функция для перевода в строке 'action' в состояние 'active'"""

        queryset.update(is_active=True)


@admin.register(DateRoute)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной Дате, определенного Направления."""

    filter_horizontal = ['direction_name']  # для наглядной демонстрации используемых маршрутов в день
    list_display = ("date_route", "view_time_trips_link", "is_active",)
    sortable_by = ("date_route",)
    list_filter = ("date_route", "is_active")
    actions = (
        "make_inactive",
    )

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

    @admin.action(description="Switch to inactive state")
    def make_inactive(self, request, queryset):
        """Функция для проверки даты с текущей и если данная дата уже прошла, то переводим выбранные неподходящие даты

        в строке 'action' в состояние 'inactive'"""
        # today = datetime.datetime(2023, 4, 6).date() - необходимо для тестирования
        # today = datetime.datetime.now().date()
        # for obj in queryset:
        #     date = obj.date_route
        #     if date < today:
        #         print('del obj in queryset')
        # queryset.update(is_active=False)


@admin.register(TimeTrip)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретных временных отметках, в
    которые возможно отправление."""

    form = ContactForm
    list_display = ("departure_time", "date_of_the_trip", "direction", "view_trips_link", "number_of_seats",
                    "show_reserved_places", "show_free_places", "show_pretty_price", "car", "auto_number",
                    "carrier_phone")
    sortable_by = ("departure_time", "date_of_the_trip", "direction", "number_of_seats")
    list_filter = ("departure_time", "date_of_the_trip", "direction")
    actions = (
        "export_to_csv",
    )

    @admin.display(description="custom price")
    def show_pretty_price(self, obj):
        """Функция для отображения кастомной записи для 'цены за место' (В данном случае добавили знак $)"""

        return f"{obj.price} BYN"

    @admin.display(description="reserved places")
    def show_reserved_places(self, obj):
        """Функция для отображения кастомной записи для количества зарезервированных мест в данной поездке"""

        trip_from_time = obj.trip_set.all()
        sum_places = 0
        if trip_from_time:
            sum_places = sum(
                list(map(lambda trip: trip.number_of_reserved_places, trip_from_time))
            )
        return f"{sum_places}"

    @admin.display(description="free places")
    def show_free_places(self, obj):
        """Функция для отображения кастомной записи для количества свободных мест в данной поездке"""

        count_free_places = obj.number_of_seats - int(self.show_reserved_places(obj))
        return f"{count_free_places}"

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
    def export_to_csv(self, request, queryset):
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
        writer.writerow([field.verbose_name for field in fields if hasattr(field, 'verbose_name')])
        # Записываем строку для каждого объекта
        for obj in queryset:
            data_row = [getattr(obj, field.name) for field in fields if field.name != 'trip']
            writer.writerow(data_row)
        return response


@admin.register(Trip)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной поездке в определенное время."""

    list_display = ("username", "date_of_the_trip", "departure_time", "number_of_reserved_places",
                    "landing_place", "user_comment", "get_price", "get_full_price", "get_list_stops")
    sortable_by = ()
