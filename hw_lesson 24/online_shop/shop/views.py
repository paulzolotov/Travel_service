from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from .models import Game, Category, Comment
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CommentModelForm
from django.contrib.auth.decorators import login_required
from difflib import get_close_matches
from django.contrib.auth.models import User
import datetime
from .tasks import replace_text_with_censored, shop_logger_task
from django.core import serializers


# Create your views here.
def order_index(request: HttpRequest, order_by=''):
    """Функция предназначена для перехода к основной странице с играми"""
    search_name = request.GET.get('q')
    if search_name:  # Параметр поиска - необходим для поиска игры на странице
        games = Game.objects.filter(is_active=True).filter(name__icontains=search_name)
        # Можно использовать get_close_matches вместо name__icontains, но необходимо будет менять поведение в template.
        # games1 = get_close_matches(search_name, possibilities=list(dict(list(
        # Game.objects.values_list('name', 'slug')))))
    else:
        games = Game.objects.filter(is_active=True)
    if order_by != '':  # Сортировка игр. Если не указана сортировка, показывает в стандартном виде.
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
               'order_by': order_by}
    shop_logger_task.delay(str(request.path), str(request.user), datetime.datetime.now())  # task в celery
    return render(request, 'shop/games_home_page.html', context=context)


def categories(request: HttpRequest):
    """Функция предназначена для перехода к странице со списком категорий"""
    categories = Category.objects.filter(is_active=True).all()
    shop_logger_task.delay(str(request.path), str(request.user), datetime.datetime.now())  # task в celery
    return render(request, 'shop/categories.html', context={'categories': categories})


def get_game(request: HttpRequest, game_slug):
    """Функция предназначена для перехода к странице определенной игры. Игра выбирается по значению slug"""
    game = get_object_or_404(Game, slug=game_slug)
    # Узнаем есть ли у данного пользователя комм. Логика в html файле такая - если есть комм, то нет кнопки добавить.
    # Пришлось добавить условие т.к появляется ошибка если пользователь не вошел при переходе ни игру
    if request.user.is_authenticated:  # Разделяем все комм. на комм. пользов. и остальные, для того чтобы комм. в
        # дальнейшем был всегда первым
        author_comment = game.comment_set.order_by('-pub_date').filter(author=request.user)
        another_comments = game.comment_set.order_by('-pub_date').exclude(author=request.user).all()
    else:
        author_comment = None
        another_comments = game.comment_set.order_by('-pub_date').all()
    # Необходимо для отображения COOKIES, последнего посещения и кол-ва посещений страницы с игрой
    last_visited = request.COOKIES.get(game_slug + '_time_' + str(request.user))
    view_count = int(request.COOKIES.get(game_slug + '_view_' + str(request.user), 0))
    context = {'game': game,
               'another_comments': another_comments,
               'author_comment': author_comment,
               'last_visited': last_visited,
               'view_count': view_count}
    response = render(request, 'shop/game_page.html', context=context)
    visit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response.set_cookie(game_slug + '_time_' + str(request.user), visit_time, max_age=datetime.timedelta(days=20))
    response.set_cookie(game_slug + '_view_' + str(request.user), view_count+1, max_age=datetime.timedelta(days=20))
    shop_logger_task.delay(str(request.path), str(request.user), datetime.datetime.now())  # task в celery
    return response


@login_required(login_url='users:login', redirect_field_name='next')
def get_category(request: HttpRequest, category_slug):
    """Функция предназначена для перехода к странице со списком игр определенной категории игры. Категория выбирается
    по slug.login_required запрещает посещение данной страницы, если не выполнен вход пользователя в систему.
    Перенаправляет на страницу с логином. После успешного входа возвращает страницу с играми категории"""
    category = get_object_or_404(Category, slug=category_slug)
    # games_from_category = Game.objects.all().filter(is_active=True, category=category)
    #  Получение всех игр категории с помощью связанных запросов
    games_from_category = category.game_set.filter(is_active=True).all()
    shop_logger_task.delay(str(request.path), str(request.user), datetime.datetime.now())  # task в celery
    return render(request, 'shop/category_page.html', context={'games_from_category': games_from_category,
                                                       'category': category})


class CommentCreateView(CreateView):
    """Класс для добавления комментария пользователя."""
    model = Comment
    form_class = CommentModelForm  # либо form_class либо fields

    def get_success_url(self):
        """URL, на который будет произведено перенаправление"""
        return reverse("shop:game", kwargs={'game_slug': self.object.game.slug})

    def form_valid(self, form):
        """Функция для проверки валидности и использования нецензурных выражений"""
        form.instance.game = Game.objects.get(slug=self.kwargs['game_slug'])
        form.instance.author = self.request.user
        self.object = form.save()
        # Вызов .delay() является самым быстрым способом отправки сообщения о задаче в Celery
        replace_text_with_censored.delay(serializers.serialize('json', [self.object]))
        return HttpResponseRedirect(self.get_success_url())


class CommentUpdateView(UpdateView):
    """Класс для обновления комментария пользователя."""
    model = Comment
    form_class = CommentModelForm


class CommentDeleteView(DeleteView):
    """Класс для удаления комментария пользователя."""
    model = Comment
    success_url = reverse_lazy("shop:index")
