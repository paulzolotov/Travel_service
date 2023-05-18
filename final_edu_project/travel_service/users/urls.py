from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import forms, views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            next_page="booking:index", template_name="users/login.html"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="booking:index"),
        name="logout",
    ),
    path(
        "change-pass/",
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy(
                "users:password_change_done"
            ),  # Куда буду перенаправлен после успешной смены пароля,
            # можно перенаправить и на главную страницу. Указан стандартный, переопределил из-за app_name = 'users'.
            template_name="users/password_change.html",  # шаблон, использующейся для отображения
            form_class=forms.CustomPasswordChangeForm,
        ),  # форма, которая передается в шаблон
        name="change",
    ),
    path(
        "change-pass-confirm/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_success.html"
        ),
        name="password_change_done",
    ),
    path(
        "password-reset",
        auth_views.PasswordResetView.as_view(
            email_template_name="users/password_reset_mail.html",
            template_name="users/password_reset.html",
            success_url=reverse_lazy("users:pass-reset-done"),
        ),
        name="pass-reset",
    ),
    path(
        "password-reset-done",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="pass-reset-done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy("users:reset_complete"),
            template_name="users/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="reset_complete",
    ),
    path("info-edit", views.user_edit, name="user-info-edit"),
]
