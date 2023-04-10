from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class UserRegisterView(LoginView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'user/login.html'

    # def post(self, requests, *args, **kwargs):
    #     form = CustomUserCreationForm()
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.save()
    #     else:
    #         return render(requests, self.template_name, {'form': form})
