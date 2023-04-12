from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CustomUserCreationForm
from .models import BookingUser


# class UserRegisterView(LoginView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('index')
#     template_name = 'user/login.html'
#
#     # def post(self, requests, *args, **kwargs):
#     #     form = CustomUserCreationForm()
#     #     if form.is_valid():
#     #         user = form.save(commit=False)
#     #         user.save()
#     #     else:
#     #         return render(requests, self.template_name, {'form': form})
#
#     # def form_valid(self, form):
#     #     username = form.cleaned_data['username']
#     #     email = form.cleaned_data['email']
#     #     raw_password = form.cleaned_data['password1']
#     #     user = BookingUser.objects.create_user(username, email, raw_password)
#     #     login(self.request, user)
#     #     return HttpResponseRedirect(reverse('index'))


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
