from django.contrib import admin
from django.urls import path
import personas.views

urlpatterns = [
    path('', personas.views.index, name='url_index'),

#login 

    path('entrar/', personas.views.entrar, name='entrar'),
    path('salir/', personas.views.salir, name='salir'),
    path('crear_usuario/', personas.views.crear_usuario, name='crear_usuario'),


#persona
    path('listar_ficha_medica/', personas.views.persona_index, name='persona_index'),
    path('listar_ficha_medica_inactiva/', personas.views.persona_inactivo_index, name='persona_inactivo_index'),    
    path('crear_ficha_medica/', personas.views.persona_crear, name='persona_crear'),
    path('ver_ficha_medica/<int:id>/', personas.views.persona_ver, name='persona_ver'),
    path('editar_ficha_medica/<int:id>/', personas.views.persona_editar, name='persona_editar'),
    path('activar_ficha_medica/<int:id>/', personas.views.persona_activar, name='persona_activar'),
    path('desactivar_ficha_medica/<int:id>/', personas.views.persona_desactivar, name='persona_desactivar'),
    path('eliminar_ficha_medica/<int:id>/', personas.views.persona_eliminar, name='persona_eliminar'),
    path('buscar_ficha_medica/', personas.views.persona_buscar, name='persona_buscar'),


]
