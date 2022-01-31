from django import formss
from django import forms 
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.ChaField(required=True)

    class Meta:
        model = Dweet
        exclude = ("user",)