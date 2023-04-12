from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class BookingUser(AbstractUser):
    phone = PhoneNumberField(null=True)
    date_of_birth = models.DateTimeField(verbose_name='Date of birth', null=True)
    cookie_consent = models.BooleanField(default=True, verbose_name="Do you agree to the use of cookies?")
