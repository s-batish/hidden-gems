from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form to add a review
    """
    class Meta:
        model = Review
        fields = ('body',)
        labels = {
            'body': 'Please write your review here'
        }
