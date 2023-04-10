from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy
from . views import UserRegisterView

from . import forms, views

app_name = "users"

urlpatterns = [
    path(
        "register/",
        UserRegisterView.as_view(),
        name="register"),
]
