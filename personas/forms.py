from django.forms import ModelForm
from django import forms
# from django.forms import widgets
# from django.forms.widgets import Widget
from personas.models import Persona
import datetime


#-------------------------
# Personas
#-------------------------

class Persona_Form(ModelForm):
    '''Especificacion de campos para este formulario'''
    class Meta:
        model = Persona
        fields = [
            'primer_nombre', 'otros_nombres', 'apellido_paterno', 'apellido_materno', 'invertir_apellidos', #'nombre_completo',
            'rut', 'estado_civil', 'fecha_nac',
            'fono_fijo', 'fono_movil1', 'fono_movil2',
            'email', 'direccion', 'ciudad',
            'observaciones',
        ]
       
        widgets = {
            'primer_nombre': forms.TextInput(attrs={'class':'form-control'}),
            'otros_nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            'invertir_apellidos': forms.BooleanField(attrs={}),
            #'nombre_completo': forms.TextInput(attrs={'class':'form-control'}),
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nac': forms.DateField(initial=datetime.date.today),
            'fono_fijo': forms.TextInput(attrs={'class':'form-control'}),
            'fono_movil1': forms.TextInput(attrs={'class':'form-control'}),
            'fono_movil2': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'observaciones': forms.TextInput(attrs={'class':'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super(Persona_Form, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        
