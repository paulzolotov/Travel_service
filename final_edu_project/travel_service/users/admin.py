from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import BookingUser


class CustomUserAdmin(UserAdmin):
    """Класс, необходимый для отображения в admin панели кастомных полей пользователя"""

    model = BookingUser
    add_form = CustomUserCreationForm

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
