from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(next_page='shop:index', template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='shop:index'), name='logout'),
]