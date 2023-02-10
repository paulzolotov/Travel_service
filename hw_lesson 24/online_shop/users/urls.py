from django.urls import path, include, reverse_lazy

from django.contrib.auth import views as auth_views
from . import views
from . import forms

app_name = 'users'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(next_page='shop:index', template_name='users/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='shop:index'), name='logout'),
    path('change-pass/', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('users:password_change_done'),  # Куда буду перенаправлен после успешной смены пароля,
        # можно перенаправить и на главную страницу. Указан стандартный, переопределил из-за app_name = 'users'.
        template_name='users/password_change.html',  # шаблон, использующейся для отображения
        form_class=forms.CustomPasswordChangeForm),  # форма, которая передается в шаблон
        name='change'),
    path('change-pass-confirm/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_success.html'),
        name='password_change_done')
]
