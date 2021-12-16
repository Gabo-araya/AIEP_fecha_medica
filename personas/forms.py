from django.forms import ModelForm
from django import forms
# from django.forms import widgets
# from django.forms.widgets import Widget
from personas.models import Persona



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
       

    def __init__(self, *args, **kwargs):
        super(Persona_Form, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        

