from django import forms

from .models import Trip
from users.models import BookingUser


class TripModelForm(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Должно было поменять пустое поле в выборе остановки на "Остановка не выбрана"
        self.fields['landing_place'].empty_label = "Остановка не выбрана"

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
