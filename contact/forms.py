from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form to contact Hidden Gems
    """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message',)
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'messsage': 'Please leave your query here',
        }
