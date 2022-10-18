from django import forms
from django.db.models import fields
from App_Desafio.models import familiar


class FormularioFamiliar(forms.ModelForm):

    class Meta():
        model = familiar
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type':'date'})}

        
        