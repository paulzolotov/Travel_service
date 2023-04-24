from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:direction_slug>/<date_route>/", views.get_daytime_trip, name="direction"),
    path("<slug:direction_slug>/<date_route>/<int:trip_id>/success", views.booking_success, name="trip-success"),
    path("<slug:direction_slug>/<date_route>/<int:trip_id>/", views.TripCreateView.as_view(), name="trip"),
    path("contacts", views.contacts, name="contacts"),
    # path("account", views.account, name="account"),
]
