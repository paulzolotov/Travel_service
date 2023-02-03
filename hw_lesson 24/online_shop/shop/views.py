from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Game, Category, Comment
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


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
    print(games, page_number, page_obj, sep='\n')
    return render(request, 'shop/games_home_page.html', context={'page_obg': page_obj,
                                                                 'order_by': order_by})


def categories(request: HttpRequest):
    categories = Category.objects.filter(is_active=True).all()
    return render(request, 'shop/categories.html', context={'categories': categories})


def get_game(request: HttpRequest, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    comments = game.comment_set.all()
    return render(request, 'shop/game_page.html', context={'game': game,
                                                           'comments': comments})


def get_category(request: HttpRequest, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    # games_from_category = Game.objects.all().filter(is_active=True, category=category)
    #  Получение всех игр категории с помощью связанных запросов
    games_from_category = category.game_set.filter(is_active=True).all()
    return render(request, 'shop/category_page.html', context={'games_from_category': games_from_category,
                                                       'category': category})


# def form_practice(request):
#     if request.method == 'POST':
#         form = CommentModelForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#         else:
#             form = CommentModelForm()
#     return render(request, 'store/practice.html', {'form': form})


class CommentCreateView(CreateView):
    model = Comment
    fields = ["text", "rating"]

    def form_valid(self, form):
        form.instance.game = Game.objects.get(slug=self.kwargs['game_slug'])
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ["text", "rating"]


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("shop:index")
