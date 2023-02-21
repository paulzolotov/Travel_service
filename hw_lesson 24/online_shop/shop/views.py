from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Game, Category, Comment
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CommentModelForm
from django.contrib.auth.decorators import login_required
from difflib import get_close_matches
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.core.cache import cache


# Create your views here.
def order_index(request: HttpRequest, order_by=''):
    search_name = request.GET.get('q')
    if search_name:  # Необходимо для поиска игры на странице
        # Добавил кеширование всех игр
        # cache_games = cache.get('games')
        # if not cache_games:
            games = Game.objects.filter(is_active=True).filter(name__icontains=search_name)
            # cache.set('games', games, 60*5)
        # Можно использовать get_close_matches вместо name__icontains, но необходимо будет менять поведение в template.
        # games1 = get_close_matches(search_name, possibilities=list(dict(list(
        # Game.objects.values_list('name', 'slug')))))
    else:
        # Добавил кеширование всех игр
        # cache_games = cache.get('games')
        # if not cache_games:
            games = Game.objects.filter(is_active=True)
            # cache.set('games', games, 60*5)
    if order_by != '':
        sorting_dict = {
            'price-asc': games.order_by('-price'),
            'name-asc': games.order_by('name'),
            'price-desc': games.order_by('price'),
            'name-desc': games.order_by('-name'),
        }
        games = sorting_dict.get(order_by)
    paginator = Paginator(games, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj,
               'order_by': order_by,
               'paginator': paginator}
    return render(request, 'shop/games_home_page.html', context=context)


def categories(request: HttpRequest):
    categories = Category.objects.filter(is_active=True).all()
    return render(request, 'shop/categories.html', context={'categories': categories})


def get_game(request: HttpRequest, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    # Узнаем есть ли у данного пользователя комм. Логика в html файле такая - если есть комм, то нет кнопки добавить.
    # Пришлось добавить условие т.к появляется ошибка если пользователь не вошел при переходе ни игру
    if request.user.is_authenticated:
        author_comment = game.comment_set.order_by('-pub_date').filter(author=request.user)
        another_comments = game.comment_set.order_by('-pub_date').exclude(author=request.user).all()
    else:
        author_comment = None
        another_comments = game.comment_set.order_by('-pub_date').all()
    context = {'game': game,
               'another_comments': another_comments,
               'author_comment': author_comment}
    return render(request, 'shop/game_page.html', context=context)


@login_required(login_url='users:login', redirect_field_name='next')
def get_category(request: HttpRequest, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    # games_from_category = Game.objects.all().filter(is_active=True, category=category)
    #  Получение всех игр категории с помощью связанных запросов
    games_from_category = category.game_set.filter(is_active=True).all()
    return render(request, 'shop/category_page.html', context={'games_from_category': games_from_category,
                                                       'category': category})


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentModelForm  # либо form_class либо fields

    def form_valid(self, form):
        form.instance.game = Game.objects.get(slug=self.kwargs['game_slug'])
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentModelForm


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("shop:index")
