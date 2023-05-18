import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travel_service.settings")
app = Celery("travel_service")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Выполняет задание каждый день в 00:00
app.conf.beat_schedule = {
    "daily_check_of_today_for_activity": {
        "task": "booking.tasks.make_inactive_last_day_task",
        "schedule": crontab(minute=0, hour=0),
    },
    # 'daily_check_of_today_for_activity_test': {
    #     'task': 'booking.tasks.make_inactive_last_day_task',
    #     'schedule': 3,
    # },
    "check_elapsed_trip_time": {
        "task": "booking.tasks.make_inactive_at_timetrip_task",
        "schedule": crontab(),
    },
}
app.conf.timezone = "UTC"
