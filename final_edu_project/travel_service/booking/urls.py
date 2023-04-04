from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("", views.index, name="index"),
    # path("<slug:direction>", views.get_direction, name="direction"),
    # path("<slug:direction>/<slug:day>", views.order_index, name="rout"),
    # path("contacts", views.contacts, name="contacts"),
    # path("account", views.account, name="account"),
]
