from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import ValidationError


class CustomUserCreationForm(UserCreationForm):
    """Класс для создания формы по регистрации пользователя"""
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={"class": "form-input"})
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
        fields = UserCreationForm.Meta.fields + ("email",)


class CustomPasswordChangeForm(PasswordChangeForm):
    """Класс для создания формы по смене пароля"""
    old_password = forms.CharField(
        label="Old Password", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password1 = forms.CharField(
        label="New Password", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password2 = forms.CharField(
        label="New Password confirmation",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )

    def clean(self):
        """Функция для проверки несовпадения нового пароля и старого"""
        cleaned_data = super().clean()
        user = self.user
        new = cleaned_data.get("new_password1")
        if user.check_password(new):
            raise ValidationError("The new password is the same as the old one.")
