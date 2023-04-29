from django.urls import path, re_path

from . import views

urlpatterns = [
    path("directions/", views.GetDirectionInfoView.as_view()),
    path("dateroutes/", views.GetDateRouteInfoView.as_view()),
    path("timetrips/", views.GetTimeTripInfoView.as_view()),
    path(
        "info/<slug:direction_slug>/<date_route>/",
        views.DirectionDateRouteView.as_view(),
    ),
    path("filter-timetrips/", views.GetTimeTripInfoFilterView.as_view()),
    path("search-timetrips/", views.GetTimeTripInfoSearchView.as_view()),
    path("order-timetrips/", views.GetTimeTripInfoOrderView.as_view()),
]
