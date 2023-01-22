from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.order_index, name='index'),
    path('?order_by=<order_by>', views.order_index, name='or-index'),
    path('categories/', views.categories, name='categories'),
    path('game/<slug:game_slug>/', views.get_game, name='game'),
    path('<slug:category_slug>/', views.get_category, name='category')
]