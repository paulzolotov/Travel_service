from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.order_index, name='index'),
    path('?order_by=<order_by>', views.order_index, name='or-index'),
    path('categories/', views.categories, name='categories'),
    path('game/<slug:game_slug>/comment/', views.CommentCreateView.as_view(), name='comment-add'),
    path('game/<slug:game_slug>/', views.get_game, name='game'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('<slug:category_slug>/', views.get_category, name='category'),
]
