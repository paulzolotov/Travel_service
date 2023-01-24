from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun_index, name='index'),
    path('skills/', views.fun_skills, name='skills'),
    path('edu/', views.fun_edu, name='edu'),
    ]