from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Game, Category
from decimal import Decimal


# Create your views here.
def index(request: HttpRequest, category_id):
    sorting = request.GET.get('sorting')
    sorting_by_category = Game.objects.filter(category=category_id)
    sorting_dict = {
        'price': sorting_by_category.order_by('price'),
        'name': sorting_by_category.order_by('name')
    }
    # return render(request, 'shop/home_page.html', games)
    return HttpResponse(sorting)


def categories(request: HttpRequest):
    categories = Category.objects.all().values()
    return HttpResponse(categories)


def get_game(request: HttpRequest, *args, **kwargs):
    game_slug = kwargs.get('game_slug')
    game = Game.objects.all().values().filter(slug=game_slug)
    print(game[0]['game_image'])
    return render(request, 'shop/game_page.html', {'game': game})


def get_category(request: HttpRequest, *args, **kwargs):
    category_slug = kwargs.get('category_slug')
    category = Category.objects.get(slug=category_slug)
    games_from_category = Game.objects.all().values().filter(category=category)
    return HttpResponse(games_from_category)
