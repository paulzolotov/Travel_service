from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CustomUserCreationForm, CustomUserUpdateForm


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


@login_required(login_url="users:login", redirect_field_name="next")
def user_edit(request: HttpRequest) -> HttpRequest:
    """Функция предназначена для перехода к странице для редактирования контактной информацией"""

    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(reverse("booking:account"))
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(
        request,
        "users/user_info_edit.html",
        context={"form": form},
    )
