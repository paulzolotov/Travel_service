from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Game, Category
from decimal import Decimal


# Create your views here.
def order_index(request: HttpRequest, order_by='without'):
    sorting_dict = {
        'price-asc': Game.objects.filter(is_active=True).order_by('-price'),
        'name-asc': Game.objects.filter(is_active=True).order_by('name'),
        'price-desc': Game.objects.filter(is_active=True).order_by('price'),
        'name-desc': Game.objects.filter(is_active=True).order_by('-name'),
        'without': Game.objects.filter(is_active=True)
    }
    games = sorting_dict.get(order_by)
    return render(request, 'shop/games_home_page.html', {'games': games})


def categories(request: HttpRequest):
    categories = Category.objects.filter(is_active=True).all()
    return render(request, 'shop/categories.html', context={'categories': categories})


def get_game(request: HttpRequest, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    print(game.game_image.url)
    return render(request, 'shop/game_page.html', context={'game': game})


def get_category(request: HttpRequest, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    games_from_category = Game.objects.all().filter(category=category)
    print(games_from_category)
    return render(request, 'shop/category_page.html', context={'games_from_category': games_from_category,
                                                       'category': category})
