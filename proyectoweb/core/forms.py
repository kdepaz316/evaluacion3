from django import forms
from django.forms import ModelForm
from .models import Persona

class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['Id'].required = False
        self.fields['Rut'].required = False
        self.fields['nombre'].required = False
        self.fields['apellido'].required = False
        self.fields['categoria'].required = False
    class Meta:
        model = Persona
        fields = ['Id','Rut','nombre','apellido','categoria',]