from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Travel Service API",
        default_version="v1",
        description="Travel Service where you can booking one or several places in different directories, "
        "dates and time.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@busby.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
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
