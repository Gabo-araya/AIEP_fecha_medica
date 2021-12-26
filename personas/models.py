from django.db import models
# from model_utils import Choices
# from tinymce import models as tinymce_models


#=======================================================================================================================================
# Table `Personas`
#=======================================================================================================================================

class Persona(models.Model):

    #fk_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Usuario', help_text='Está conectado con el modelo User de la autenticación de Django. No tocar.') # user
    
    primer_nombre = models.CharField(max_length=50, verbose_name='Primer nombre', help_text='')
    otros_nombres = models.CharField(max_length=50, null=True, blank=True, verbose_name='Otros nombres', help_text='')
    apellido_paterno = models.CharField(max_length=50, verbose_name='Apellido paterno', help_text='')
    apellido_materno = models.CharField(max_length=50, verbose_name='Apellido materno', help_text='')
    invertir_apellidos = models.BooleanField(default=False, null=True, blank=True, verbose_name='Invertir apellidos', help_text='Esta opción permite poner el apellido materno antes del apellido paterno.')
    nombre_completo = models.CharField(max_length=250, null=True, blank=True, verbose_name='Nombre completo', help_text='')

    rut = models.CharField(max_length=10, null=True, blank=True, verbose_name='Rut', help_text='Rut con dígito verificador. Formato: 12345678-9')
    estado_civil = models.CharField(max_length=50, null=True, blank=True, verbose_name='Estado Civil', help_text='')
    fecha_nac = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento', help_text='')

    fono_fijo = models.CharField(max_length=10, null=True, blank=True, verbose_name='Teléfono Fijo', help_text='Formato: 12 3456 7890')
    fono_movil1 = models.CharField(max_length=9, null=True, blank=True, verbose_name='Teléfono Móvil 1', help_text='Formato: 9 1234 5678')
    fono_movil2 = models.CharField(max_length=9, null=True, blank=True, verbose_name='Teléfono Móvil 2', help_text='Formato: 9 1234 5678')

    email  = models.EmailField(max_length=250, null=True, blank=True, verbose_name='Email')
    direccion = models.TextField(null=True, blank=True, verbose_name='Dirección', help_text='')
    ciudad = models.CharField(max_length=50, null=True, blank=True, verbose_name='Ciudad', help_text='')

    observaciones = models.TextField(null=True, blank=True, verbose_name='Observaciones', help_text='Escriba sus observaciones.')

    activo  = models.BooleanField(null=True, blank=True, default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Fecha de última modificación')
    deleted = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de desactivación')

    class Meta:
        ''' class Meta:
            Define el nombre singular y plural, y el ordenamiento de los elementos
        '''
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['-id']

    def field_name(self):
        ''' def field_name(self):
            Retorna un string que será el nombre que mostrará el objeto 
        '''
        if self.invertir_apellidos == True:
            return str('{} {} {} {} [{}]'. format(self.primer_nombre, self.otros_nombres, self.apellido_materno, self.apellido_paterno, self.rut))
        else:
            return str('{} {} {} {} [{}]'. format(self.primer_nombre, self.otros_nombres, self.apellido_paterno, self.apellido_materno, self.rut))
            # return '{} {} {} {}'. format(self.primer_nombre, self.segundo_nombre, self.apellido_paterno, self.apellido_materno)

    def __str__(self):
        ''' def __str__(self):
            Retorna un string con el nombre del objeto en las listas y en el admin
        '''
        return self.field_name()



