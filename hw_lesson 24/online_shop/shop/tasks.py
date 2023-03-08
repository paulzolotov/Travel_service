import datetime
from better_profanity import profanity
import time
from django.core import serializers
from celery import shared_task
from termcolor import colored
import logging

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


logger = logging.getLogger(__name__)


@shared_task()
def shop_logger_task(path: str, user: str, time):
    """Функция предназначена для логирования основных запросов магазина. Расположенных во sop/views.py"""
    logger.info(time + ' | ' + path + ' | ' + user)
    # print(colored(time + ' | ' + path + ' | ' + user, 'red'))

