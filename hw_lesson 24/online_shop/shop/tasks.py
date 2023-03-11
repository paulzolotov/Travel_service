from better_profanity import profanity
import time
from django.core import serializers
from celery import shared_task
from termcolor import colored
import logging
from .models import Log
from django.core.mail import send_mail
from django.urls import reverse_lazy
from typing import List
from .models import Game
from django.contrib.auth.models import User
import datetime

profanity.load_censor_words()


@shared_task()
def replace_text_with_censored(instance):
    """Функция предназначена для цензурирования комментариев пользователей"""
    instance = list(serializers.deserialize('json', instance))[0].object  # из json строки будем преобразовывать в
    # объект django orm. Чтобы достать сам объект комментария исп. object
    censored_text = profanity.censor(instance.text)
    time.sleep(5)  # имитация бурной деятельности
    instance.text = censored_text
    instance.save()


logger = logging.getLogger(__name__)  # необходимо для логгинга


@shared_task()
def shop_logger_task(path: str, user: str, time):
    """Функция предназначена для логирования основных запросов магазина. Расположенных во sop/views.py"""
    logger.info(time + ' | ' + path + ' | ' + user)
    # print(colored(time + ' | ' + path + ' | ' + user, 'red'))
    Log(path=path, user=user, datetime=time).save()  # Добавление лога в БД


@shared_task()
def send_news_email_task(games: List[dict], top3_rating_games: dict, user: dict):
    """Функция для еженедельной отправки сообщения об играх пользователям. Ч1"""
    message_text = f'Hello {user["username"]}! See all our updates from last week!\n'
    for game in games:
        msg_chunk = f"""
        {game['name']} added at {game['release_date']}, price - {game['price']}
        More details: {reverse_lazy("shop:game", args=game['slug'])}
        """
        message_text += msg_chunk
    message_text += '\nAlso, we have prepared for you the Top 3 games with the best rating for the last week.\n'
    count = 1
    for game, rating in top3_rating_games.items():
        msg_game_rating = f"""
        {count}. {game} - {rating}
        """
        message_text += msg_game_rating
        count += 1
    send_mail(
        "Weekly news",  # тема письма
        message_text,
        "support@example.com",  # от кого письмо
        [user['email']],  # кому письмо
        fail_silently=False,  # чтобы не вызывалась ошибка, что email не удалось отправить(при возникновении ошибки)
    )


@shared_task()
def weekly_notification_task():
    """Функция для еженедельной отправки сообщения об играх пользователям. Ч2
        Делали 2 функции разные, т.к. может произойти сбой в celery, отправке сообщения на email и т.д
        чтобы это избежать разделяем для каждого пользователя создается отдельное письмо(задание).
        В таком случае может не отправиться одно письмо, но оно не повлияет на другие для других пользователей"""
    all_users = list(User.objects.filter(is_staff=False).values())  # выбираем пользователей, которые не имеют
    # staff status (права). ДОПОЛНИТЕЛЬНО можно реализовать фильтрацию по признаку согласия рассылки
    # (т.е при регистрации спрашивать у пользователя - хочет ли получать еженедельную рассылку)
    all_new_games = list(Game.objects.filter(
        pub_date__gte=datetime.datetime.today()-datetime.timedelta(days=7)).values())  # получаем игры, добавленные
    # за последние 7 дней
    # Получаем 3 игры с наивысшем рейтингом
    rating_games = {game.name: game.get_average_rating()['rating__avg']
                    if game.get_average_rating()['rating__avg'] is not None
                    else 0.0 for game in Game.objects.filter(is_active=True)}  # Получили словарь ключ в котором
    # является название игры, а значение это ее рейтинг. Если рейтинга нет, то использовал 0.0.
    top3_rating_games = dict(sorted(rating_games.items(), key=lambda item: item[1], reverse=True)[:3])  # Отсортировали
    # словарь, по значениям т.е. от самого большого значения до самого маленького, взяли только первые 3 пары ключ-знач.
    for user in all_users:
        send_news_email_task.delay(all_new_games, top3_rating_games, user)  # для каждого пользователя отправляем письмо
