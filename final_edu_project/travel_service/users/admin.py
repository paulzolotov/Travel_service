from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import BookingUser


class CustomUserAdmin(UserAdmin):
    model = BookingUser
    add_form = CustomUserCreationForm  # не подтянуло другие поля

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


admin.site.register(BookingUser, CustomUserAdmin)
