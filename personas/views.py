from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.core.paginator import Paginator
from personas.models import Persona
from personas.forms import Persona_Form, CustomUserCreationForm
import calendar, datetime


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# define la cantidad de elementos de la página inicial
cantidad_elementos = '5'
asdf = ''

# ======================================
# LOGIN Y REGISTRO
# ======================================

def entrar(request, *args, **kwargs):
    '''Página de Lotin del sitio web. '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('url_index')

    context = {
        # 'cantidad' : cantidad,
        'page' : 'Acceso a Sistema de Fichas Médicas',
    }

    return render(request, 'login.html', context)



def salir(request, *args, **kwargs):
    logout(request)
    return redirect('entrar')



@login_required(login_url='entrar')
def crear_usuario(request, *args, **kwargs):

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('url_index')

    context = {
        # 'cantidad' : cantidad,
        'page' : 'Crear usuario',
        'form': form,
    }

    return render(request, 'personas/generic_form.html', context)




# ======================================
# PAGINAS GENERALES
# ======================================

@login_required(login_url='entrar')
def index(request, *args, **kwargs):
    '''Página inicial del sitio web. Debe contener vínculos a los usuarios y a las fichas médicas.'''
   
    queryset = Persona.objects.filter(activo=True)[:50] # escoger los últimos 50
    # queryset = Persona.objects.all() # Lista de objetos
    # id_perfil = 1
    # qs_perfil = PerfilPersonal.objects.filter(id=id_perfil)
    # qs_perfil = PerfilPersonal.objects.get(id=1)

    # qs_actividadlaboral = ActividadLaboral.objects.filter(erased=False)[:5] 
    # qs_proyecto = Proyecto.objects.filter(erased=False)[:5] 
    # qs_actividadacademica = ActividadAcademica.objects.filter(tipo_estudio='CARRERA_PREGRADO') | ActividadAcademica.objects.filter(tipo_estudio='CARRERA_POSGRADO') & ActividadAcademica.objects.filter(erased=False)[:5]
    # qs_perfeccionamiento = ActividadAcademica.objects.filter(tipo_estudio='PERFECCIONAMIENTO') | ActividadAcademica.objects.filter(tipo_estudio='CURSO') | ActividadAcademica.objects.filter(tipo_estudio='OTRO_ESTUDIO') & ActividadAcademica.objects.filter(erased=False)
    # qs_perfeccionamiento = qs_perfeccionamiento[:5]  # escoger los últimos 5
    # qs_area_interes = AreaInteres.objects.filter(erased=False)
    # qs_tecnologia = Tecnologia.objects.filter(erased=False)

    # print(qs_area_interes)
    # qs_perfil = PerfilPersonal.objects.filter(erased=False)
    
    # print(qs_perfil[0].url_github)
    # print(qs_perfil.url_github)

    # Lista de objetos
    # qs_ = PerfilPersonal.objects.filter(activo=True) # Lista de objetos
    # qs_perfil = PerfilPersonal.objects.filter(activo=True) # Lista de objetos
    # qs_perfil = PerfilPersonal.objects.filter(activo=True) # Lista de objetos
    # cantidad = queryset.count() #necesario para el total
    # cantidad debe traer sólo los elementos activos. 
    
    # print(qs_perfeccionamiento[1].fk_tecnologias)
    
    context = {
        # 'cantidad' : cantidad,
        'page' : 'Ficha médica',
        'description' : '',
        'icon' : 'person',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'url_activo_index' :'persona_index',
        'url_inactivo_index' : 'persona_inactivo_index',
        'url_crear' : 'persona_crear',
        'url_ver' : 'persona_ver',
        'url_editar' : 'persona_editar',
        'url_desactivar' : 'persona_desactivar',
        'url_activar' : 'persona_activar',
        'url_eliminar' : 'persona_eliminar',
        'asdf' : asdf,
        'object_list': queryset,
        # 'obj_actividadlaboral': qs_actividadlaboral,
        # 'obj_actividadacademica': qs_actividadacademica,
        # 'obj_perfeccionamiento': qs_perfeccionamiento,
        # 'obj_proyecto': qs_proyecto,
        # 'obj_area_interes': qs_area_interes,
        # 'obj_tecnologia': qs_tecnologia,
        
    }

    return render(request, 'personas/persona_index.html', context)


# ======================================
# PERSONAS
# ======================================

@login_required(login_url='entrar')
def persona_index(request, *args, **kwargs):
    '''Página inicial del sitio web.'''
   
    # queryset = Persona.objects.all() # Lista de objetos
    queryset = Persona.objects.filter(activo=True)[:50] # escoger los últimos 50

    context = {
        # 'cantidad' : cantidad,
        'page' : 'Fichas médicas',
        'description' : 'Se puede ver la lista de fichas médicas',
        'icon' : 'person',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'url_activo_index' :'persona_index',
        'url_inactivo_index' : 'persona_inactivo_index',
        'url_crear' : 'persona_crear',
        'url_ver' : 'persona_ver',
        'url_editar' : 'persona_editar',
        'url_desactivar' : 'persona_desactivar',
        'url_activar' : 'persona_activar',
        'url_eliminar' : 'persona_eliminar',
        'asdf' : asdf,
        'object_list': queryset,
    }

    return render(request, 'personas/persona_index.html', context)



@login_required(login_url='entrar')
def persona_inactivo_index(request, *args, **kwargs):
    '''Lista de elementos inactivos con las que se pueden realizar acciones.'''
    #queryset = Persona.objects.all() # Lista de objetos
    queryset = Persona.objects.filter(activo=False) # Lista de objetos
    cantidad = queryset.count() #necesario para el total
    paginator = Paginator(queryset, cantidad_elementos) 
    page_number = request.GET.get('pag')
    page_obj = paginator.get_page(page_number)
    context = {
        'page' : 'Fichas médicas inactivas',
        'description' : '',
        'icon' : 'person',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'url_activo_index' : 'persona_index',
        'url_inactivo_index' : 'persona_inactivo_index',
        'url_crear' : 'persona_crear',
        'url_ver' : 'persona_ver',
        'url_editar' : 'persona_editar',
        'url_desactivar' : 'persona_desactivar',
        'url_activar' : 'persona_activar',
        'url_eliminar' : 'persona_eliminar',
        'asdf' : asdf,
        'cantidad' : cantidad,
        'object_list': page_obj
    }
    return render(request, 'personas/persona_index.html', context)



@login_required(login_url='entrar')
def persona_ver(request, id, *args, **kwargs):
    '''Sirve para revisar un elemento.'''
    itemObj = Persona.objects.get(id=id)
    
    context = {
        'page' : 'Revisar ficha médica',
        'description' : 'Se pueden ver todas las características de la ficha médica',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'url_activo_index' :'persona_index',
        'url_inactivo_index' : 'persona_inactivo_index',
        'url_crear' : 'persona_crear',
        'url_ver' : 'persona_ver',
        'url_editar' : 'persona_editar',
        'url_desactivar' : 'persona_desactivar',
        'url_activar' : 'persona_activar',
        'url_eliminar' : 'persona_eliminar',
        'asdf' : asdf,
        'item': itemObj
    }
    return render(request, 'personas/persona_ver.html', context)



@login_required(login_url='entrar')
def persona_crear(request, *args, **kwargs):
    '''Sirve para crear un elemento.'''
    form = Persona_Form

    if request.method == 'POST':
        form = Persona_Form(request.POST, request.FILES)
        if form.is_valid():
            #print('form')

            form.save()
            return redirect('persona_index')

    context = {
        'page' : 'Crear ficha médica',
        'description' : 'Rellene el formulario y presione el botón guardar para crear una nueva ficha médica.',
        'icon' : 'person',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'asdf' : asdf,
        'form': form,
    }
    return render(request, 'personas/generic_form.html', context)



@login_required(login_url='entrar')
def persona_editar(request, id, *args, **kwargs):
    '''Sirve para editar un elemento.'''
    itemObj = Persona.objects.get(id=id)
    form = Persona_Form(instance=itemObj)

    if request.method == 'POST':
        form = Persona_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():

            #guardar form
            form.save()
            return redirect('persona_index')

    context = {
        'page' : 'Editar ficha médica',
        'description' : 'Realice las modificaciones que estime convenientes.',
        'icon' : 'person',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'asdf' : asdf,
        'item': itemObj,
        'form': form
    }
    return render(request, 'personas/generic_form.html', context)



@login_required(login_url='entrar')
def persona_activar(request, id, *args, **kwargs):
    '''Sirve para activar un elemento.'''
    itemObj = Persona.objects.get(id=id)

    if request.method == 'POST':
        itemObj.activo = '1'
        itemObj.deleted = None

        itemObj.save()
        return redirect('persona_index')

    context = {
        'page' : 'Activar ficha médica',
        'description' : 'El elemento volverá a estar disponible para modificar.',
        'icon' : 'person',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'asdf' : asdf,
        'item': itemObj
    }
    return render(request, 'personas/activar_objetos.html', context)



@login_required(login_url='entrar')
def persona_desactivar(request, id, *args, **kwargs):
    '''Sirve para desactivar un elemento.'''
    itemObj = Persona.objects.get(id=id)

    if request.method == 'POST':
        itemObj.activo = '0'
        itemObj.deleted = datetime.datetime.now()

        itemObj.save()
        return redirect('persona_index')
        #else:
        #    print('algo falló al guardar')

    context = {
        'page' : 'Desactivar ficha médica',
        'description' : 'El elemento ya no estará disponible para modificar.',
        'icon' : 'person',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'asdf' : asdf,
        'item': itemObj
    }
    return render(request, 'personas/desactivar_objetos.html', context)



@login_required(login_url='entrar')
def persona_eliminar(request, id, *args, **kwargs):
    '''Sirve para eliminar un elemento.'''
    itemObj = Persona.objects.get(id=id)
    
    if request.method == 'POST':

        itemObj.delete()
        return redirect('persona_index')

    context = {
        'page' : 'Eliminar ficha médica',
        'description' : 'Esta acción no se puede deshacer.',
        'icon' : 'person',
        'singular' : 'ficha médica',
        'plural' : 'fichas médicas',
        'asdf' : asdf,
        'item': itemObj
    }
    return render(request, 'personas/eliminar_objetos.html', context)



@login_required(login_url='entrar')
def persona_buscar(request, *args, **kwargs):
    '''Lista de elementos encontrados con los que se pueden realizar acciones.'''

    busqueda = ''
    resultado = ''

    if request.method == 'POST':

        busqueda = request.POST['busqueda']
        resultado = Persona.objects.filter(primer_nombre__icontains=busqueda) | Persona.objects.filter(otros_nombres__icontains=busqueda) | Persona.objects.filter(apellido_paterno__icontains=busqueda) | Persona.objects.filter(apellido_materno__icontains=busqueda) | Persona.objects.filter(rut__icontains=busqueda) & Persona.objects.filter(activo=True)

        context = {
            'page' : 'Fichas médicas encontradas',
            'description' : '',
            'icon' : 'person',
            'singular' : 'ficha médica',
            'plural' : 'fichas médicas',
            'url_activo_index' : 'persona_index',
            'url_inactivo_index' : 'persona_inactivo_index',
            'url_crear' : 'persona_crear',
            'url_ver' : 'persona_ver',
            'url_editar' : 'persona_editar',
            'url_desactivar' : 'persona_desactivar',
            'url_activar' : 'persona_activar',
            'url_eliminar' : 'persona_eliminar',
            'asdf' : asdf,
            #'cantidad' : cantidad,
            'busqueda' : busqueda,
            'object_list': resultado
        }
        #return redirect('persona_buscar')
        return render(request, 'personas/persona_buscar.html', context)
    else:
        return redirect('persona_index')

