# Ficha Médica

_Sistema web sobre fichas médicas desarrollado con Django 3.2 para Taller de Testing y Calidad de Software._

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

## Pre-requisitos 📋

_Esta es una lista de los paquetes que deben estar instalados previamente:_

* Python 3
	- Lenguaje de programación
	- [Ayuda - https://docs.microsoft.com/en-us/windows/python/beginners)](https://docs.microsoft.com/en-us/windows/python/beginners)
	- [Curso Django desde Cero en youtube](https://www.youtube.com/watch?v=vo4VF3neyrs)
* Pip
	- Gestor de instalación de paquetes PIP
	- [Ayuda - https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/)
* Virtualenv
	- Creador de entornos virtuales para Python
	- [Ayuda - https://techexpert.tips/es/windows-es/instalacion-del-entorno-virtual-de-python-en-windows/](https://techexpert.tips/es/windows-es/instalacion-del-entorno-virtual-de-python-en-windows/)

## Instalación pre-requisitos 🔧

Muchas veces tenemos ese problema común de no poder instalar ciertas librerías o realizar configuraciones para poder desarrollar en Windows para Web y es por ello que en éste tutorial vamos a ver los pasos para instalar Python y configurarlo con Pip y Virtualenv para así poder empezar a desarrollar aplicaciones basadas en éste lenguaje e instalar Django prontamente para crear aplicaciones web. [Ver video -> **https://www.youtube.com/watch?v=sG7Q-r_SZhA**](https://www.youtube.com/watch?v=sG7Q-r_SZhA)

1. Descargamos e instalamos Python 3.4 para Windows
	- [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Agregaremos Python a las variables de entorno de nuestro sistema si es que no se agregaron durante la instalación para que así podamos ejecutarlo desde la terminal `/cmd`
	- `C:\Python34 y C:\Python34\Scripts`

3. Ejecutamos Pip para verificar que esté instalado correctamente y también la versión
	- `pip --version`

4. Instalamos Virtualenv con
	- `pip install virtualenv`

5. Verificamos la versión de Virtualenv
	- `virtualenv --version`

6. Crearemos un entorno virtual con Python
	- `virtualenv test`

7. Iniciamos el entorno virtual
	- `.\test\Scripts\activate`

8. Finalmente desactivamos el entorno virtual
	- `deactivate`

## Instalación Local 🚀

Seguir los siguientes pasos para la instalación local.

1. Clonar el repositorio.

	- `git clone https://github.com/Gabo-araya/AIEP_testing/`

2. Instalar los requerimientos.

	- `python3 -m pip install -r requirements.txt`

3. Revisar settings.py
	- Revisar que la sección de base de datos esté configurada para que trabaje con la base de datos SQLite en local.

3. Realizar migraciones
	- Crear archivos de migración: `python3 manage.py makemigrations`
	- Realizar migraciones`python3 manage.py migrate`

4. Crear superusuario
	- `python3 manage.py createsuperuser`

5. Iniciar el servidor
	- `python3 manage.py runserver`
	- Iniciar en un puerto específico (:9500):`python3 manage.py runserver 9500`

## Despliegue 📦

_Aquí van notas adicionales sobre como hacer deploy_

Para el despliegue en Google Cloud Platform, seguir los pasos que aparecen acá: [https://bennettgarner.medium.com/deploying-a-django-application-to-google-app-engine-f9c91a30bd35](https://bennettgarner.medium.com/deploying-a-django-application-to-google-app-engine-f9c91a30bd35)

## Construido con 🛠️

_Estas son las herramientas que hemos utilizado en nuestro proyecto_

* [Django](https://www.djangoproject.com/) - El framework web usado
* [Consola Google Cloud](https://console.cloud.google.com//) - La plataforma de destino

## Autores ✒️

* **Gabo Araya** - *BackEnd y documentación* - [Gabo-araya](https://github.com/Gabo-araya/)
* **Lucas Rubilar** - *FrontEnd y documentación* - [Lucas ](https://github.com/Gabo-araya/)
* **David Torcates** - *FrontEnd y documentación* - [DavidTorcates](https://github.com/DavidTorcates/)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto.

