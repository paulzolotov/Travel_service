from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class BookingUser(AbstractUser):
    carrier_phone = PhoneNumberField(null=True)
    date_of_birth = models.DateTimeField(verbose_name='Date of birth', null=True)
