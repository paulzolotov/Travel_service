from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.GetGameInfoView.as_view()),
    path('games/<str:category>', views.GetCategoryGamesInfoView.as_view()),
    path('categories/', views.GetCategoryInfoView.as_view()),
]
