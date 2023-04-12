from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import SelectDateWidget
from django.forms import ValidationError
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField

from .models import BookingUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """Класс для создания формы по регистрации пользователя"""

    phone = PhoneNumberField(
        label="Номер телефона",
        region='BY',
        widget=PhoneNumberPrefixWidget(
            country_choices=[
                ("BY", "375"),
                ("RU", "7"),
                ("UA", "380")
            ],
        ),
    )
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    first_name = forms.CharField(
        label="Имя", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    last_name = forms.CharField(
        label="Фамилия", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    date_of_birth = forms.DateField(
        label="Дата рождения", widget=SelectDateWidget(years=range(1940, 2010))
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    cookie_consent = forms.BooleanField(label="Вы соглашаетесь с размещением файлов cookie на вашем компьютере, "
                                              "с целью анализа использования Веб-сайта?",
                                        initial=1,
                                        widget=forms.CheckboxInput(attrs={"class": "form-input"}))

    class Meta(UserCreationForm.Meta):
        """Добавляем доп. поле"""

        model = BookingUser
        fields = ("phone", "username", "first_name", "last_name", "email", "date_of_birth", "password1", "password2",
                  "cookie_consent")


class CustomPasswordChangeForm(PasswordChangeForm):
    """Класс для создания формы по смене пароля"""

    old_password = forms.CharField(
        label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password1 = forms.CharField(
        label="Новый пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )

    def clean(self):
        """Функция для проверки несовпадения нового пароля и старого"""
        cleaned_data = super().clean()
        user = self.user
        new = cleaned_data.get("new_password1")
        if user.check_password(new):
            raise ValidationError("Новый пароль совпадает со старым.")
