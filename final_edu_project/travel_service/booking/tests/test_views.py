from booking.models import Direction
from django.test import TestCase
from django.urls import reverse


class DirectionsTestsClass(TestCase):
    """Класс для тестирования представлений"""

    @classmethod
    def setUpTestData(cls):
        """Выполняется перед запуском всех тестов конкретного класса"""

        number_of_games = 3
        for game_num in range(1, number_of_games):
            Direction.objects.create(
                slug="minsk_pinsk",
                name="Минск-Пинск",
                start_point="Минск",
                end_point="Пинск",
                list_of_stops="Rest.1, Rest.2",
                travel_time=220,
                is_active=True,
            )

    def test_view_url_exists_at_desired_location(self):
        """Тестирование корректного перехода"""

        resp = self.client.get("/booking/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Тестирование корректности названия представления"""

        resp = self.client.get(reverse("booking:index"))
        self.assertEqual(resp.status_code, 200)
