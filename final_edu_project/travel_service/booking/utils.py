import datetime

from .tasks import booking_logger_task


def decorator_log(func):
    """Декоратор для логгинга."""

    def wrapper(*args, **kwargs):
        """Обертка"""
        request = args[0]
        booking_logger_task.delay(
            request.path, request.user.username, datetime.datetime.now()
        )
        return func(*args, **kwargs)

    return wrapper
