from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CustomUserCreationForm
from .models import BookingUser


def register(request):
    """Функция для регистрации пользователя"""
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("booking:index"))
        else:
            form = CustomUserCreationForm(request.POST)
        return render(request, "users/register.html", {"form": form})
