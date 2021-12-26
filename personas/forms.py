from django import forms
from django.forms import ModelForm, Textarea, CheckboxInput

# importaciones para usuarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# from django.forms import widgets
# from django.forms.widgets import Widget

from personas.models import Persona
import datetime

#-------------------------
# Usuarios
#-------------------------

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese el usuario...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese el password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirme el password...'})

#-------------------------
# Personas
#-------------------------

class Persona_Form(ModelForm):
    '''Especificacion de campos para este formulario'''
    class Meta:
        model = Persona
        fields = [
            'primer_nombre', 
            'otros_nombres', 
            'apellido_paterno', 
            'apellido_materno', 
            'invertir_apellidos', 
            #'nombre_completo',
            'rut', 
            'estado_civil', 
            'fecha_nac',
            'fono_fijo', 
            'fono_movil1', 
            'fono_movil2',
            'email', 
            'direccion', 
            'ciudad',
            'observaciones',
        ]
       
        widgets = {
            'primer_nombre': forms.TextInput(attrs={'class':'form-control'}),
            'otros_nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            #'invertir_apellidos': forms.BooleanField(attrs={'class':'form-check-input'}),
            
            'invertir_apellidos': CheckboxInput(attrs={'class':'form-check-input'}),

            
            #'nombre_completo': forms.TextInput(attrs={'class':'form-control'}),
            'rut': forms.TextInput(attrs={'class':'form-control'}),

            #'estado_civil': forms.Select(attrs={'class':'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class':'form-control'}),
            
            # 'fecha_nac': forms.SelectDateWidget(empty_label=("Año", "Mes", "Día"),attrs={'class':'fecha'}),
            'fecha_nac': forms.DateInput(attrs={'class':'form-control'}),

            'fono_fijo': forms.NumberInput(attrs={'class':'form-control'}),
            'fono_movil1': forms.NumberInput(attrs={'class':'form-control'}),
            'fono_movil2': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'direccion': Textarea(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'observaciones': Textarea(attrs={'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(Persona_Form, self).__init__(*args, **kwargs)
        
        #self.fields['']
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class':'form-control'})
        
