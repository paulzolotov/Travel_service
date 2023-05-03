import datetime

from django.core.files.base import File
from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_tripticket(user_email: str, ticket_name: str, date: str) -> None:
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
