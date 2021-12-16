from django.contrib import admin
from django.urls import path
import personas.views

urlpatterns = [
    path('', personas.views.index, name='url_index'),


#persona
    path('listar_ficha_medica/', personas.views.persona_index, name='persona_index'),
    path('listar_ficha_medica_inactiva/', personas.views.persona_inactivo_index, name='persona_inactivo_index'),    
    path('crear_ficha_medica/', personas.views.persona_crear, name='persona_crear'),
    path('ver_ficha_medica/<int:id>/', personas.views.persona_ver, name='persona_ver'),
    path('editar_ficha_medica/<int:id>/', personas.views.persona_editar, name='persona_editar'),
    path('activar_ficha_medica/<int:id>/', personas.views.persona_activar, name='persona_activar'),
    path('desactivar_ficha_medica/<int:id>/', personas.views.persona_desactivar, name='persona_desactivar'),
    path('eliminar_ficha_medica/<int:id>/', personas.views.persona_eliminar, name='persona_eliminar'),


]
