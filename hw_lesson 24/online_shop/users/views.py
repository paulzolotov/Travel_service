from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CustomUserCreationForm


# Create your views here.
def register(request):
    """Функция для регистрации пользователя"""
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("shop:index"))
        else:
            form = CustomUserCreationForm(request.POST)
        return render(request, "users/register.html", {"form": form})
