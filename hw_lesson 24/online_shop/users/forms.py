from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ValidationError


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='New Password confirmation', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))

    def clean(self):
        cleaned_data = super().clean()
        user = self.user
        new = cleaned_data.get('new_password1')
        if user.check_password(new):
            raise ValidationError('The new password is the same as the old one.')
