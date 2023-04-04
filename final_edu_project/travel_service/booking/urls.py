from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:direction_slug>/<slug:date_route>", views.get_direction, name="direction"),
    path("contacts", views.contacts, name="contacts"),
    # path("account", views.account, name="account"),
]
