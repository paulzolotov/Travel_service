from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect(reverse("shop:index"))
        # return redirect(reverse("users:register"))
