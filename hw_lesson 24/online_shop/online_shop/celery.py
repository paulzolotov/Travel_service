import os
from celery import Celery
from celery.schedules import crontab
# from shop.tasks import weekly_notification_task


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')
app = Celery('online_shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app = Celery()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Выполняет задание каждый понедельник в 09:00
    # sender.add_periodic_task(crontab(hour=9, minute=00, day_of_week=1), weekly_notification.s(),
    #                          name='send_to_users_info_about_games')
    sender.add_periodic_task(crontab(), weekly_notification_task.s(), name='send_to_users_info_about_games')
