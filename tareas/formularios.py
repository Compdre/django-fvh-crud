from django.forms import ModelForm
from django import forms
from .models import t_tareas

class f_creatareas(forms.ModelForm):
    class Meta:
        model  = t_tareas
        fields = ['titulo','descripcion','importante']
        widgets={
            'titulo':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escriba un título'}),
            'descripcion':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escriba la descripción'}),  
            'importante':forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
          }