from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Game, Category
from decimal import Decimal


# Create your views here.
def index(request: HttpRequest):
    # sorting = request.GET.get('sorting')
    # sorting_by_category = Game.objects.filter(category=category_id)
    # sorting_dict = {
    #     'price': sorting_by_category.order_by('price'),
    #     'name': sorting_by_category.order_by('name')
    # }
    # return render(request, 'shop/home_page.html', games)
    games = Game.objects.filter(is_active=True).all()
    return render(request, 'shop/games_home_page.html', {'games': games})


def categories(request: HttpRequest):
    categories = Category.objects.filter(is_active=True).all()
    return render(request, 'shop/categories.html', {'categories': categories})


def get_game(request: HttpRequest, *args, **kwargs):
    game_slug = kwargs.get('game_slug')
    game = Game.objects.all().filter(slug=game_slug)
    print(game[0].game_image.url)
    return render(request, 'shop/game_page.html', {'game': game[0]})


def get_category(request: HttpRequest, *args, **kwargs):
    category_slug = kwargs.get('category_slug')
    category = Category.objects.get(slug=category_slug)
    games_from_category = Game.objects.all().filter(category=category)
    print(games_from_category)
    return render(request, 'shop/category_page.html', {'games_from_category': games_from_category,
                                                       'category': category})
