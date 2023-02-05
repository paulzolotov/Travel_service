from django import forms
from django.core.validators import EmailValidator
from .models import Comment


class GameSearchForm(forms.Form):

    available_choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    comment = forms.CharField(max_length=50, help_text='Enter comment')
    game_rating = forms.CharField(choices=available_choices)


class CommentModelForm(forms.ModelForm):
    def clean_rating(self):
        rating = self.cleaned['rating']
        if rating < 0:
            raise forms.ValidationError('Only positive marks are allowed')

    class Meta:
        model = Comment
        exclude = ['pub_date', 'game']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
            'rating': forms.NumberInput(attrs={'class': 'number-select'})
        }
        labels = {
            'text': 'Comment text',
        }
        help_texts = {
            'text': 'Please, rate this game for better experience'
        }
