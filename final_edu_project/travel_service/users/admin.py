from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BookingUser

admin.site.register(BookingUser)
