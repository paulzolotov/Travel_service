from django import forms
from django.contrib.auth.forms import (PasswordChangeForm, UserChangeForm,
                                       UserCreationForm)
from django.forms import SelectDateWidget, ValidationError
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import BookingUser


class CustomUserFieldsMixinFrom(forms.Form):
    """Класс Mixin, для повторяющихся полей пользователя, от которого затем наследуются классы с формами"""

    phone = PhoneNumberField(
        label="Номер телефона",
        region="BY",
        widget=PhoneNumberPrefixWidget(
            attrs={"class": "form__input"},
            country_choices=[("BY", "375"), ("RU", "7"), ("UA", "380")],
        ),
    )
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form__input"})
    )
    first_name = forms.CharField(
        label="Имя", widget=forms.TextInput(attrs={"class": "form__input"})
    )
    last_name = forms.CharField(
        label="Фамилия", widget=forms.TextInput(attrs={"class": "form__input"})
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form__input"})
    )
    cookie_consent = forms.BooleanField(
        label="Вы соглашаетесь с размещением файлов cookie на вашем компьютере, "
        "с целью анализа использования Веб-сайта?",
        initial=1,
        widget=forms.CheckboxInput(attrs={"class": "form__input form__input-check"}),
    )


class CustomUserCreationForm(UserCreationForm, CustomUserFieldsMixinFrom):
    """Класс для создания формы по регистрации пользователя"""

    date_of_birth = forms.DateField(
        label="Дата рождения",
        widget=SelectDateWidget(
            years=range(1940, 2010), attrs={"class": "form__input"}
        ),
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form__input"})
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form__input"}),
    )

    class Meta(UserCreationForm.Meta):
        """Добавляем доп. поле"""

        model = BookingUser
        fields = (
            "phone",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "password1",
            "password2",
            "cookie_consent",
        )


class CustomPasswordChangeForm(PasswordChangeForm):
    """Класс для создания формы по смене пароля"""

    old_password = forms.CharField(
        label="Старый пароль",
        widget=forms.PasswordInput(attrs={"class": "form__input"}),
    )
    new_password1 = forms.CharField(
        label="Новый пароль", widget=forms.PasswordInput(attrs={"class": "form__input"})
    )
    new_password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form__input"}),
    )

    def clean(self) -> None:
        """Функция для проверки несовпадения нового пароля и старого"""
        cleaned_data = super().clean()
        user = self.user
        new = cleaned_data.get("new_password1")
        if user.check_password(new):
            raise ValidationError("Новый пароль совпадает со старым.")


class CustomUserUpdateForm(UserChangeForm, CustomUserFieldsMixinFrom):
    """Класс для создания формы по редактированию информации пользователя"""

    password = None  # для того чтобы убрать отображение поля password в форме

    class Meta(UserCreationForm.Meta):
        """Добавляем доп. поле"""

        model = BookingUser
        fields = (
            "phone",
            "username",
            "first_name",
            "last_name",
            "email",
            "cookie_consent",
        )
        exclude = ("password",)
