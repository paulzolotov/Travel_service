from django import forms

from .models import Trip


class TripModelForm(forms.ModelForm):
    """Форма для модели Trip"""

    def __int__(self, *args, **kwargs):
        """Изменение параметров формы при инициализации"""

        super().__init__(*args, **kwargs)
        # Должно было поменять пустое поле в выборе остановки на "Остановка не выбрана"
        self.fields["landing_place"].empty_label = "Остановка не выбрана"

    class Meta:
        model = Trip
        fields = ["number_of_reserved_places", "landing_place", "user_comment"]
        widgets = {
            "number_of_reserved_places": forms.NumberInput(
                attrs={"class": "booking__form-input booking__form-input__num"}
            ),
            "landing_place": forms.Select(attrs={"class": "booking__form-input"}),
            "user_comment": forms.Textarea(
                attrs={"class": "booking__form-input booking__form-input__area"}
            ),
        }
        labels = {
            "number_of_reserved_places": "Кол-во забронированных мест",
            "landing_place": "Остановка",
            "user_comment": "Комментарий",
        }
