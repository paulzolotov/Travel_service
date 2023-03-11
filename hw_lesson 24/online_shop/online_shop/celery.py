import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')
app = Celery('online_shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# Выполняет задание каждый понедельник в 09:00
app.conf.beat_schedule = {
    'send_mail_at_9_monday': {
        'task': 'shop.tasks.weekly_notification_task',
        'schedule': crontab(hour=9, minute=00, day_of_week=1),
    },

    # 'send_mail_test': {
    #     'task': 'shop.tasks.weekly_notification_task',
    #     'schedule': 60,
    # },
}
app.conf.timezone = 'UTC'
