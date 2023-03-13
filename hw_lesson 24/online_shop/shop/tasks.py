import datetime
from better_profanity import profanity
import time
from django.core import serializers
from celery import shared_task
from termcolor import colored
import logging
from .models import Log

profanity.load_censor_words()


@shared_task()
def replace_text_with_censored(instance):
    """Функция предназначена для цензурирования комментариев пользователей"""
    instance = list(serializers.deserialize('json', instance))[0].object  # из json строки будем преобразовывать в
    # объект django orm. Чтобы достать сам объект комментария исп. object
    censored_text = profanity.censor(instance.text)
    instance.text = censored_text
    instance.save()


logger = logging.getLogger(__name__)


@shared_task()
def shop_logger_task(path: str, user: str, time):
    """Функция предназначена для логирования основных запросов магазина. Расположенных во shop/views.py"""
    logger.info(time + ' | ' + path + ' | ' + user)
    # print(colored(time + ' | ' + path + ' | ' + user, 'red'))
    Log(log_path=path, log_user=user, log_datetime=time).save()  # Добавление лога в БД
