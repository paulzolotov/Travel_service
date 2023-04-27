from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CustomUserCreationForm


def register(request: HttpRequest) -> HttpRequest:
    """Функция для регистрации пользователя"""
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect(reverse("booking:index"))
        else:
            form = CustomUserCreationForm(request.POST)
        return render(request, "users/register.html", {"form": form})
