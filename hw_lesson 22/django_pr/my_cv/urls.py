from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun_index, name='index'),
    path('skills/', views.fun_skills, name='skills'),
    path('edu/', views.fun_edu, name='edu'),
    path('sign-in/', views.fun_sign, name='sign-in'),
    path('skills/sign-in/', views.fun_sign, name='sign-in'),
    path('edu/sign-in/', views.fun_sign, name='sign-in')
    ]