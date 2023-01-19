from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.index, name='games'),
    path('categories/', views.categories, name='categories'),
    path('game-<slug:game_slug>/', views.get_game, name='game'),
    path('category-<slug:category_slug>/', views.get_category, name='category')
]