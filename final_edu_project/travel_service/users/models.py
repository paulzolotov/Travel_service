from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BookingUser(AbstractUser):
    phone = PhoneNumberField(null=True)
    date_of_birth = models.DateTimeField(verbose_name="Date of birth", null=True)
    cookie_consent = models.BooleanField(
        default=True, verbose_name="Do you agree to the use of cookies?"
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        """Возвращает first_name и last_name с пробелом между ними."""

        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
