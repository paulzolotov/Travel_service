import datetime
import logging

from django.core.files.base import File
from celery import shared_task
from django.core.mail import send_mail
from .models import DateRoute
from .models import Log

logger = logging.getLogger(__name__)  # необходимо для логгинга


@shared_task()
def booking_logger_task(path: str, user: str, time: datetime):
    """Функция предназначена для логирования основных запросов сервиса по бронированию, расположенных в
    booking/views.py"""

    logger.info(time + " | " + path + " | " + user)
    Log(log_path=path, log_user=user, log_datetime=time).save()  # Добавление лога в БД


@shared_task()
def send_tripticket_task(user_email: str, ticket_name: str, date: str) -> None:
    """Функция предназначена для отправления билета на поездку в pdf формате на почту пользователя"""

    with open(f'media/booking/{ticket_name}', 'rb') as f:
        send_mail(
            f"Билет на поездку {date}",  # тема письма
            '',
            "support@busby.by",  # от кого письмо
            [user_email],  # кому письмо
            html_message=f"{File(f)}",
            fail_silently=False,  # чтобы не вызывалась ошибка, что email не удалось отправить(при возникновении ошибки)
        )


@shared_task()
def make_inactive_last_day_task():
    """Функция для ежедневной проверки активных дней в сервисе. Идея такова: если день уже прошел т.е наступило 0.00
    мин нового дня и это день имел статус 'активен', переводим его в 'неактивный'
    """

    # today = datetime.datetime(2023, 4, 6).date()  # for debug
    today = datetime.datetime.now().date()
    all_dates = [x["date_route"] for x in DateRoute.objects.filter(is_active=True).values()]
    if today in all_dates:
        queryset = DateRoute.objects.filter(date_route=today)
        print(queryset)
        queryset.update(is_active=False)
