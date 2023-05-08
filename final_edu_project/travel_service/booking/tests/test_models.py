import datetime

from booking.models import DateRoute, Direction
from django.test import TestCase


class DirectionsTestsClass(TestCase):
    """Класс для тестирования модели Direction"""

    @classmethod
    def setUpTestData(cls):
        """Выполняется перед запуском всех тестов конкретного класса"""

        cls.direction = Direction.objects.create(
            slug="minsk_pinsk",
            name="Минск-Пинск",
            start_point="Минск",
            end_point="Пинск",
            list_of_stops="Rest.1, Rest.2",
            travel_time=220,
            is_active=True,
        )

    def setUp(self):
        """Выполняется перед запуском каждого теста"""

        pass

    def tearDown(self):
        """Выполняется после завершения каждого теста"""

        pass

    # Тесты ссылаются на ошибки с экземплярами моделей
    def test_slug_verbose_name(self):
        """Функция, проверяющая название параметра verbose_name атрибута Direction - slug"""

        real_verbose_name = getattr(self.slug, "verbose_name")
        expected_verbose_name = "Short Name"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_slug_max_length(self):
        """Функция, проверяющая длину параметра max_length атрибута Direction - slug"""

        real_max_length = getattr(self.slug, "max_length")
        self.assertEqual(real_max_length, 70)

    def test_name_verbose_name(self):
        """Функция, проверяющая название параметра verbose_name атрибута Direction - name"""

        real_verbose_name = getattr(self.name, "verbose_name")
        expected_verbose_name = "Direction Name"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_name_max_length(self):
        """Функция, проверяющая длину параметра max_length атрибута Direction - name"""

        real_max_length = getattr(self.name, "max_length")
        self.assertEqual(real_max_length, 70)


class DateRoutesTestsClass(TestCase):
    """Класс для тестирования модели DateRoute"""

    @classmethod
    def setUpTestData(cls):
        """Выполняется перед запуском всех тестов конкретного класса"""

        cls.dateroute = DateRoute.objects.create(
            date_route=datetime.datetime(2023, 4, 6).date(),
            is_active=True,
        )

    def setUp(self):
        """Выполняется перед запуском каждого теста"""

        pass

    def tearDown(self):
        """Выполняется после завершения каждого теста"""

        pass

    # Тесты ссылаются на ошибки с экземплярами моделей
    def test_date_route_verbose_name(self):
        """Функция, проверяющая название параметра verbose_name атрибута DateRoute - date_route"""

        real_verbose_name = getattr(self.date_route, "verbose_name")
        expected_verbose_name = "Date of trip"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_date_route_auto_now_add(self):
        """Функция, проверяющая длину параметра max_length атрибута DateRoute - date_route"""

        real_auto_now_add = getattr(self.date_route, "auto_now_add")
        self.assertEqual(real_auto_now_add, False)
