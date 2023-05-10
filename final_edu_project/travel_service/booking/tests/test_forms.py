from django.test import TestCase

from booking.forms import TripModelForm


class TripModelFormTest(TestCase):
    """Класс для тестирования формы TripModelForm"""

    def test_renew_form_number_of_reserved_places_label(self):
        """Функция, проверяющая название параметра label поля формы TripModelForm - number_of_reserved_places"""

        form = TripModelForm()
        self.assertTrue(form.fields['number_of_reserved_places'].label == "Кол-во забронированных мест")

    def test_renew_form_number_of_reserved_places_help_text(self):
        """Функция, проверяющая название параметра help_text поля формы TripModelForm - number_of_reserved_places"""

        form = TripModelForm()
        self.assertTrue(form.fields['number_of_reserved_places'].help_text == "")

    def test_renew_form_landing_place_label(self):
        """Функция, проверяющая название параметра label поля формы TripModelForm - landing_place"""

        form = TripModelForm()
        self.assertTrue(form.fields['landing_place'].label == "Остановка")

    def test_renew_form_landing_place_help_text(self):
        """Функция, проверяющая название параметра help_text поля формы TripModelForm - landing_place"""

        form = TripModelForm()
        self.assertTrue(form.fields['landing_place'].help_text == "")

    def test_renew_form_user_comment_label(self):
        """Функция, проверяющая название параметра label поля формы TripModelForm - user_comment"""

        form = TripModelForm()
        self.assertTrue(form.fields['user_comment'].label == "Комментарий")

    def test_renew_form_user_comment_help_text(self):
        """Функция, проверяющая название параметра help_text поля формы TripModelForm - user_comment"""

        form = TripModelForm()
        self.assertTrue(form.fields['user_comment'].help_text == "")
