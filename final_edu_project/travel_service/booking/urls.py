from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "<slug:direction_slug>/<date_route>/", views.get_daytime_trip, name="direction"
    ),
    path(
        "<slug:direction_slug>/<date_route>/<int:timetrip_id>/success",
        views.booking_success,
        name="trip-success",
    ),
    path(
        "<slug:direction_slug>/<date_route>/<int:timetrip_id>/impossible",
        views.booking_impossible,
        name="trip-impossible",
    ),
    path(
        "<slug:direction_slug>/<date_route>/<int:timetrip_id>/",
        views.TripCreateView.as_view(),
        name="trip",
    ),
    path("contacts", views.contacts, name="contacts"),
    path(
        "account/trip/remove/<int:trip_id>/",
        views.trip_remove_in_account,
        name="trip_remove",
    ),
    path("account", views.account, name="account"),
]
