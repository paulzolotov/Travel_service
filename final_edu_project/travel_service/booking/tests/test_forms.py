from django.test import TestCase

from booking.forms import TripModelForm


class TripModelFormTest(TestCase):

    def test_renew_form_date_field_label(self):
        form = TripModelForm()
        self.assertTrue(form.fields['renewal_date'].label == None)