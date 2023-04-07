from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:direction_slug>/<date_route>/", views.get_daytime_trip, name="direction"),
    path("<slug:direction_slug>/<date_route>/<int:trip_id>/", views.booking_trip, name="trip"),
    path("contacts", views.contacts, name="contacts"),
    # path("account", views.account, name="account"),
]
