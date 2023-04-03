from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("", views.order_index, name="index"),
    path("<slug:direction>", views.order_index, name="direction"),
    path("<slug:direction>/<slug:day>", views.order_index, name="rout")
]

