from django.contrib import admin
from .models import Direction, DateRoute, TimeTrip, Trip
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Register your models here.
class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'carrier_phone': PhoneNumberPrefixWidget(initial='BY'),
        }


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретном Направлении маршрута."""

    list_display = ("name", "is_active", "slug", "start_point", "end_point", "travel_time")


@admin.register(DateRoute)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной Дате, определенного Направления."""

    list_display = ("data_route", "is_active", "slug")


@admin.register(TimeTrip)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретных временных отметках, в
    которые возможно отправление."""

    list_display = ("departure_time", "date_of_the_trip", "direction", "number_of_seats", "price", "car",
                    "auto_number", "carrier_phone")
    form = ContactForm


@admin.register(Trip)
class DirectionAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной поездке в определенное время."""

    list_display = ("user_phone", "departure_time", "number_of_reserved_places", "landing_place")
