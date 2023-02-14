from django.urls import path

from . import views

urlpatterns = [
    path('games/<str:some_value>', views.GetGameInfoView.as_view()),
]
