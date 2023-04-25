from django import forms

from .models import Trip
from django.shortcuts import get_object_or_404
from .models import TimeTrip


class TripModelForm(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Должно было поменять пустое поле в выборе остановки на "Остановка не выбрана"
        self.fields['landing_place'].empty_label = "Остановка не выбрана"

    # def clean_number_of_reserved_places(self):
    #     number_of_seats = self.cleaned_data["number_of_reserved_places"]
    #     free_seats = self.departure_time.number_of_free_places_in_trip()
    #     if number_of_seats > free_seats:
    #         raise forms.ValidationError(
    #             'Осталось свободных мест: %(value)s',
    #             code='invalid',
    #             params={'value': free_seats},
    #         )
    #     return number_of_seats

    class Meta:
        model = Trip
        fields = ["number_of_reserved_places", "landing_place", "user_comment"]
        widgets = {
            "number_of_reserved_places": forms.NumberInput(attrs={"class": "number-select", "cols": 40, "rows": 4}),
            "user_comment": forms.TextInput(attrs={"class": "form-input"})
        }
        labels = {
            "text": "Comment text",
        }
        help_texts = {"text": "Please, rate this game for better experience"}
