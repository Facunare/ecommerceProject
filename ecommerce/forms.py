from django import forms
from django.forms import ModelForm
from .models import stockProducts
class stockForm(ModelForm):
    class Meta:
        model = stockProducts
        fields = ['nom_prod', 'cant_prod', 'precio_prod']