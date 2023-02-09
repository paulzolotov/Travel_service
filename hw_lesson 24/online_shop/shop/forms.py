from django import forms
from .models import Comment


class CommentModelForm(forms.ModelForm):
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 0 or rating > 10:
            raise forms.ValidationError('The number must be between 1 and 10')
        return rating

    class Meta:
        model = Comment
        exclude = ['pub_date', 'game']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'rating': forms.NumberInput(attrs={'class': 'number-select'}),
            # 'author': forms.TextInput(attrs={'readonly': 'readonly'})
        }
        labels = {
            'text': 'Comment text',
        }
        help_texts = {
            'text': 'Please, rate this game for better experience'
        }
