from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .forms import CustomUserCreationForm
from .models import BookingUser


class CustomUserAdmin(UserAdmin):
    """Класс, необходимый для отображения в admin панели кастомных полей пользователя"""

    model = BookingUser
    add_form = CustomUserCreationForm
    list_display = (
        "username",
        "view_time_trips_link",
        "first_name",
        "last_name",
        "email",
        "is_staff",
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "User additional fields",
            {
                "fields": (
                    "phone",
                    "date_of_birth",
                    "cookie_consent",
                )
            },
        ),
    )

    @admin.display(description="user_trips")
    def view_time_trips_link(self, obj):
        """Функция для подсчета количества поездок у пользователя"""

        count = obj.trip_set.count()
        url = (
            reverse("admin:booking_trip_changelist")
            + "?"
            + urlencode({"username_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Trips</a>', url, count)


admin.site.register(BookingUser, CustomUserAdmin)
