from booking.models import Direction
from django.test import TestCase
from django.urls import reverse
from users.models import BookingUser


class DirectionsTestsClass(TestCase):
    """Класс для тестирования представлений"""

    @classmethod
    def setUpTestData(cls):
        """Выполняется перед запуском всех тестов конкретного класса"""

        number_of_directions = 3
        for direction in range(1, number_of_directions):
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

        self.user = BookingUser.objects.create_user(
            "john", "lennon@thebeatles.com", "johnpassword"
        )

    def test_view_url_exists_at_desired_location_booking(self):
        """Тестирование корректного перехода"""

        resp = self.client.get("/booking/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_booking(self):
        """Тестирование корректности названия представления"""

        resp = self.client.get(reverse("booking:index"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_booking(self):
        """Тестирование корректности отображения шаблона"""

        resp = self.client.get(reverse("booking:index"))
        self.assertTemplateUsed(resp, "booking/index.html")

    def test_view_url_exists_at_desired_location_contacts(self):
        """Тестирование корректного перехода"""

        resp = self.client.get("/booking/contacts")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_contacts(self):
        """Тестирование корректности названия представления"""

        resp = self.client.get(reverse("booking:contacts"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_contacts(self):
        """Тестирование корректности отображения шаблона"""

        resp = self.client.get(reverse("booking:contacts"))
        self.assertTemplateUsed(resp, "booking/contacts.html")

    def test_view_url_exists_at_desired_location_account(self):
        """Тестирование корректного перехода"""

        self.client.login(username="john", password="johnpassword")
        resp = self.client.get("/booking/account")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_account(self):
        """Тестирование корректности названия представления"""

        self.client.login(username="john", password="johnpassword")
        resp = self.client.get(reverse("booking:account"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_account(self):
        """Тестирование корректности отображения шаблона"""

        self.client.login(username="john", password="johnpassword")
        resp = self.client.get(reverse("booking:account"))
        self.assertTemplateUsed(resp, "booking/account.html")
