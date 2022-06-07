from django import forms
from .models import *

class LibroForm(forms.ModelForm):
    class Meta:
        model = libreria
        fields = '__all__'