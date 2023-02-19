from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.GetGameInfoView.as_view()),
    path('games/<str:category>', views.GetCategoryGamesInfoView.as_view()),
    path('categories/', views.GetCategoryInfoView.as_view()),
    path('filter-games/', views.GetGameInfoFilterView.as_view()),
    path('search-games/', views.GetGameInfoSearchView.as_view()),
    path('order-games/', views.GetGameInfoOrderView.as_view()),
]
