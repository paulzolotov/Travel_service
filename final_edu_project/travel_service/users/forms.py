from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    """Класс для создания формы по регистрации пользователя"""

    first_name = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    last_name = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    email = forms.EmailField(
        label="Email address", widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    phone_number = forms.EmailField(
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

        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "phone_number", "email",)
