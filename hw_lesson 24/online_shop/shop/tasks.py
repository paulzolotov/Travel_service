import datetime
from django.http import HttpRequest
from better_profanity import profanity
import time
from django.core import serializers
from celery import shared_task
from termcolor import colored

profanity.load_censor_words()


@shared_task()
def replace_text_with_censored(instance):
    instance = list(serializers.deserialize('json', instance))[0].object  # из json строки будем преобразовывать в
    # объект django orm. Чтобы достать сам объект комментария исп. object
    censored_text = profanity.censor(instance.text)
    time.sleep(5)  # имитация бурной деятельности
    instance.text = censored_text
    instance.save()


@shared_task()
def shop_logger_task(request: HttpRequest):
    print(serializers.deserialize('json', request))
    print(list(serializers.deserialize('json', request)))
    request = list(serializers.deserialize('json', request))
    time_now = str(datetime.datetime.now())
    path = str(request.path)
    user = str(request.user)
    print(colored(time_now + ' | ' + path + ' | ' + user, 'green'))

