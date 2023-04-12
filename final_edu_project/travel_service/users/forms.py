from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget

from .models import BookingUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """Класс для создания формы по регистрации пользователя"""

    phone = forms.CharField(
        label="Phone", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    first_name = forms.CharField(
        label="First_name", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    last_name = forms.CharField(
        label="Last_name", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    date_of_birth = forms.DateField(
        label="Date of birth", widget=SelectDateWidget(years=range(1940, 2010))
    )
    email = forms.EmailField(
        label="Email address", widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )

    class Meta(UserCreationForm.Meta):
        """Добавляем доп. поле"""

        model = BookingUser
        fields = ("phone", "first_name", "last_name", "date_of_birth", "email", "password1", "password2",
                  "cookie_consent")


class CustomPasswordChangeForm:
    pass
