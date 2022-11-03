from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """This class is for processing the contact form"""

    class Meta:
        model = Contact
        fields = '__all__'
