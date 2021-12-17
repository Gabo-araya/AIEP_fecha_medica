from django.contrib import admin
from personas.models import Persona
#from import_export.admin import ImportExportModelAdmin

#class Persona_Admin(ImportExportModelAdmin):
class Persona_Admin(admin.ModelAdmin):    
    '''Define campos que se muestran y su agrupación en el admin'''
    list_display = ('id','primer_nombre','apellido_paterno','apellido_materno','rut',)
    list_display_links = ('primer_nombre','apellido_paterno','apellido_materno',)
    search_fields = ('primer_nombre','otros_nombres','apellido_paterno','apellido_materno','rut',)
    list_filter = ('activo','created')
    fieldsets = (
        ('Identificación', {
            'fields': (('primer_nombre','otros_nombres','apellido_paterno','apellido_materno','invertir_apellidos',),
                        ('rut','fecha_nac','estado_civil','activo',),
                        ('email','fono_movil1','fono_movil2','fono_fijo',),
                        ('direccion','ciudad','observaciones',),),
            #'description':'description',
            #'classes': ('collapse',),
        }),
    )

admin.site.register(Persona, Persona_Admin)