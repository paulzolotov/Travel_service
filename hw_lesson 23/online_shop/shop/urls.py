from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('?order_by=name', views.index, name='re-index'),
    path('categories/', views.categories, name='categories'),
    path('game/<slug:game_slug>/', views.get_game, name='game'),
    path('<slug:category_slug>/', views.get_category, name='category')
]