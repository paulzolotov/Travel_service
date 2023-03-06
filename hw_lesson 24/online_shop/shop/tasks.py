from better_profanity import profanity
import time
from django.core import serializers
from celery import shared_task

profanity.load_censor_words()


@shared_task
def replace_text_with_censored(instance):
    instance = list(serializers.deserialize('json', instance))[0].object
    censored_text = profanity.censor(instance.text)
    time.sleep(5)
    instance.text = censored_text
    instance.save()