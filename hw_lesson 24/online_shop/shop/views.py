from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Game, Category, Comment
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CommentModelForm


# Create your views here.
def order_index(request: HttpRequest, order_by=''):
    games = Game.objects.filter(is_active=True)
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
    all_average_rating = get_average_rating(games)
    context = {'page_obj': page_obj,
               'order_by': order_by,
               'all_average_rating': all_average_rating}
    print(all_average_rating)
    return render(request, 'shop/games_home_page.html', context=context)


def get_average_rating(games):
    """Функция для поиска среднего рейтинга в комментариях к каждой игре"""
    all_average_rating = dict()
    for game in games:
        game_comments = game.comment_set.all()
        if game_comments:
            all_average_rating[game.name] = sum(list(map(lambda comment: float(comment.rating), game_comments))) / len(
                game_comments)
        else:
            all_average_rating[game.name] = None
    return all_average_rating


def categories(request: HttpRequest):
    categories = Category.objects.filter(is_active=True).all()
    return render(request, 'shop/categories.html', context={'categories': categories})


def get_game(request: HttpRequest, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    comments = game.comment_set.order_by('pub_date').all()  # не работает сортировка комментариев:
                                                            # всегда от старых к новым
    average_rating = None
    if comments:
        average_rating = sum(list(map(lambda comment: float(comment.rating), comments))) / len(
            comments)
    context = {'game': game,
               'comments': comments,
               'average_rating': average_rating}
    return render(request, 'shop/game_page.html', context=context)


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
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentModelForm


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("shop:index")
