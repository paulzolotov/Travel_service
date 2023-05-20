import datetime
import logging
from typing import Any

from celery import shared_task
from django.core import serializers
from django.core.files.base import File
from django.core.mail import send_mail

from .models import DateRoute, Log, TimeTrip

logger = logging.getLogger(__name__)  # необходимо для логгинга


@shared_task()
def booking_logger_task(path: str, user: str, time: datetime):
    """Функция предназначена для логирования основных запросов сервиса по бронированию, расположенных в
    booking/views.py"""

    logger.info(time + " | " + path + " | " + user)
    Log(log_path=path, log_user=user, log_datetime=time).save()  # Добавление лога в БД


@shared_task()
def send_tripticket_task(user_email: str, ticket_name: str, trip: Any) -> None:
    """Функция предназначена для отправления билета на поездку в pdf формате на почту пользователя, также для
    соохранения билета в БД"""

    # десериализуем объект
    trip_d = list(serializers.deserialize("json", trip))[0].object

    with open(f"media/booking/{ticket_name}", "rb") as f:
        # отправка билета на почту
        send_mail(
            f"Билет на поездку {trip_d.date_of_the_trip}",  # тема письма
            "",
            "support@busby.by",  # от кого письмо
            [user_email],  # кому письмо
            html_message=f"{File(f)}",
            fail_silently=False,  # чтобы не вызывалась ошибка, что email не удалось отправить(при возникновении ошибки)
        )
        # Сохранение в бд билета в формате pdf
        trip_d.user_trip_ticket = File(f)
        trip_d.save()


@shared_task()
def make_inactive_last_day_task():
    """Функция для ежедневной проверки активных дней в сервисе. Идея такова: если день уже прошел т.е наступило 0.00
    мин нового дня и это день имел статус 'активен', переводим его в 'неактивный'
    """

    # today = datetime.datetime(2023, 4, 6).date()  # for debug
    today = datetime.datetime.now().date()
    all_dates = [
        x["date_route"] for x in DateRoute.objects.filter(is_active=True).values()
    ]
    if today in all_dates:
        queryset = DateRoute.objects.filter(date_route=today)
        queryset.update(is_active=False)


@shared_task()
def make_inactive_at_timetrip_task():
    """Функция для проверки прошедших по времени поездок в сервисе. Идея такова: если поездка уже прошла и эта поездка
    имела статус 'активен', переводим его в 'неактивный'
    """

    # time_now = datetime.time(9, 11)  # for debug
    time_now = datetime.time()
    all_timetrips = [
        x["departure_time"] for x in TimeTrip.objects.filter(is_active=True).values()
    ]
    for timetrip in all_timetrips:
        if timetrip < time_now:
            queryset = TimeTrip.objects.filter(departure_time=timetrip)
            queryset.update(is_active=False)
