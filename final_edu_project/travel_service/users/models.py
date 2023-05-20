from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BookingUser(AbstractUser):
    """Пользовательский класс User, необходимый для расширения возможностей базового User"""

    phone = PhoneNumberField(null=True)
    date_of_birth = models.DateField(verbose_name="Date of birth", null=True)
    cookie_consent = models.BooleanField(
        default=True, verbose_name="Do you agree to the use of cookies?"
    )
    email = models.EmailField(
        unique=True, verbose_name="Email address", null=True, blank=True
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self) -> str:
        """Возвращает first_name и last_name с пробелом между ними."""

        return "%s %s" % (self.first_name, self.last_name)
