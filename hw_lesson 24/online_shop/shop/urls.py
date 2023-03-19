from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.order_index, name="index"),
    path("?order_by=<order_by>", views.order_index, name="or-index"),
    path("categories/", cache_page(60 * 5)(views.categories), name="categories"),
    path(
        "game/<slug:game_slug>/comment/",
        views.CommentCreateView.as_view(),
        name="comment-add",
    ),
    path("game/<slug:game_slug>/", views.get_game, name="game"),
    # path("game/add/<slug:game_slug>/", views.basket_add, name="game-add"),
    path("basket/", views.basket, name="basket"),
    path("basket/add/<slug:game_slug>", views.basket_add, name="basket_add"),
    path("basket/remove/<slug:game_slug>", views.basket_remove, name="basket_remove"),
    path("basket/order", views.basket_order, name="basket_order"),
    path(
        "comment/<int:pk>/update/",
        views.CommentUpdateView.as_view(),
        name="comment-update",
    ),
    path(
        "comment/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="comment-delete",
    ),
    path("<slug:category_slug>/", views.get_category, name="category"),
    path("basket", views.basket, name="basket")
]
