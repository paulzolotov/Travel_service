import datetime

from django.shortcuts import get_object_or_404
from booking.models import DateRoute, Direction, TimeTrip
from django.test import TestCase


class DirectionsTestsClass(TestCase):
    """Класс для тестирования модели Direction"""

    @classmethod
    def setUpTestData(cls):
        """Выполняется перед запуском всех тестов конкретного класса"""

        Direction.objects.create(
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

        direction = Direction.objects.get(id=1)
        real_verbose_name = direction._meta.get_field('slug').verbose_name
        # real_verbose_name = getattr(self.slug, "verbose_name")
        expected_verbose_name = "Short Name"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_slug_max_length(self):
        """Функция, проверяющая длину параметра max_length атрибута Direction - slug"""

        direction = Direction.objects.get(id=1)
        real_max_length = direction._meta.get_field('slug').max_length
        self.assertEqual(real_max_length, 70)

    def test_name_verbose_name(self):
        """Функция, проверяющая название параметра verbose_name атрибута Direction - name"""

        direction = Direction.objects.get(id=1)
        real_verbose_name = direction._meta.get_field('name').verbose_name
        expected_verbose_name = "Direction Name"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_name_max_length(self):
        """Функция, проверяющая длину параметра max_length атрибута Direction - name"""

        direction = Direction.objects.get(id=1)
        real_max_length = direction._meta.get_field('name').max_length
        self.assertEqual(real_max_length, 70)

    def test_start_point_verbose_name(self):
        """Функция, проверяющая название параметра verbose_name атрибута Direction - start_point"""

        direction = Direction.objects.get(id=1)
        real_verbose_name = direction._meta.get_field('start_point').verbose_name
        expected_verbose_name = "Where does the route start?"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_start_point_max_length(self):
        """Функция, проверяющая длину параметра max_length атрибута Direction - start_point"""

        direction = Direction.objects.get(id=1)
        real_max_length = direction._meta.get_field('start_point').max_length
        self.assertEqual(real_max_length, 40)

    def test_end_point_verbose_name(self):
        """Функция, проверяющая название параметра verbose_name атрибута Direction - end_point"""

        direction = Direction.objects.get(id=1)
        real_verbose_name = direction._meta.get_field('end_point').verbose_name
        expected_verbose_name = "Where does the route end?"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_end_point_max_length(self):
        """Функция, проверяющая длину параметра max_length атрибута Direction - end_point"""

        direction = Direction.objects.get(id=1)
        real_max_length = direction._meta.get_field('end_point').max_length
        self.assertEqual(real_max_length, 40)

    def test_list_of_stops_verbose_name(self):
        """Функция, проверяющая название параметра verbose_name атрибута Direction - list_of_stops"""

        direction = Direction.objects.get(id=1)
        real_verbose_name = direction._meta.get_field('list_of_stops').verbose_name
        expected_verbose_name = "Enter stops separated by commas.(For example: Rest.1, Rest.2)"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_list_of_stops_max_length(self):
        """Функция, проверяющая длину параметра max_length атрибута Direction - list_of_stops"""

        direction = Direction.objects.get(id=1)
        real_max_length = direction._meta.get_field('list_of_stops').max_length
        self.assertEqual(real_max_length, 200)

    def test_list_of_stops_default(self):
        """Функция, проверяющая название параметра default атрибута Direction - list_of_stops"""

        direction = Direction.objects.get(id=1)
        real_verbose_name = direction._meta.get_field('list_of_stops').default
        expected_verbose_name = "Rest.1, Rest.2"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_travel_time_verbose_name(self):
        """Функция, проверяющая название параметра verbose_name атрибута Direction - travel_time"""

        direction = Direction.objects.get(id=1)
        real_verbose_name = direction._meta.get_field('travel_time').verbose_name
        expected_verbose_name = "Travel time in minutes"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_travel_time_default(self):
        """Функция, проверяющая длину параметра default атрибута Direction - travel_time"""

        direction = Direction.objects.get(id=1)
        real_max_length = direction._meta.get_field('travel_time').default
        self.assertEqual(real_max_length, 0)

    def test_object_name(self):
        """Функция, проверяющая название объекта"""

        direction = Direction.objects.get(id=1)
        expected_object_name = f"{direction.name}"
        self.assertEquals(expected_object_name, str(direction))


class DateRoutesTestsClass(TestCase):
    """Класс для тестирования модели DateRoute"""

    @classmethod
    def setUpTestData(cls):
        """Выполняется перед запуском всех тестов конкретного класса"""

        DateRoute.objects.create(
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

        date_route = DateRoute.objects.get(id=1)
        real_verbose_name = date_route._meta.get_field('date_route').verbose_name
        expected_verbose_name = "Date of trip"
        self.assertEqual(
            real_verbose_name, expected_verbose_name
        )  # assertEqual - предполагает, что аргументы одинаковы

    def test_date_route_auto_now_add(self):
        """Функция, проверяющая длину параметра max_length атрибута DateRoute - date_route"""

        date_route = DateRoute.objects.get(id=1)
        real_auto_now_add = date_route._meta.get_field('date_route').auto_now_add
        self.assertEqual(real_auto_now_add, False)

    def test_object_name(self):
        """Функция, проверяющая название объекта"""

        date_route = DateRoute.objects.get(id=1)
        expected_object_name = f"{date_route.date_route}"
        self.assertEquals(expected_object_name, str(date_route))
