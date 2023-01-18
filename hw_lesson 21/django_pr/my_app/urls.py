from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.fun_index, name='home'),
    path('quotes/', views.MyClassBasedViewQuote.as_view(), name='quotes'),
    path('quotes/count-<int:number>/', views.MyClassBasedViewQuote.as_view(), name='quotes'),
    path('factorial/', views.fun_factorial, name='factorial'),
    ]