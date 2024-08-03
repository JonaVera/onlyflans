# PASOS PARA CREAR UN PROYECTO

## 1. Crear carpeta y crear dentro el entorno virtual y su requirement. ##
## 2. Ejecutamos la terminal integrada de la carpeta. ##
## 3. Crear entorno virtual. ##
    --> virtualenv venv (venv nombre generico)
## 4. Activamos el entorno. ##
    --> source venv/Scripts/activate
## 5. Instalamos django. ##
    --> pip install django
* Siempre usar comandos de consultas para verificar que tenemos instalado (opcional).
    --> pip freeze // pip list
* Esto nos da las aplicaciones instaladas con sus versiones
    --> django-admin --version 
* Esto nos da la version de django
## 6. Creamos el requirements para guardar sus dependencias (aplicaciones y sus versiones) ##
    --> pip freeze > requirements.txt
## 7. Creamos el proyecto ##
    --> django-admin startproject onlyflans .
* Se crea la carpeta con sus archivos.py (modelos).
## Podemos usar manage.py para ver sus comandos que podemos usar dentro del proyecto ##
    --> python manage.py
## Tambien podemos ejecutar el proyecto, para ver su funcionamineto ##
    --> python manage.py runserver
## El proyecto ya esta levantado, ahora necesitamos sus claves y migrarlo para que no rompa el proyecto. ##
## 8. Revisamos si ya habiamos hecho migraciones ##
    --> python manage.py makemigrations
## 9. Realizamos la migracion ##
    --> python manage.py migrate
* Se migra y se abre la base de datos sqlite3, esta viene con tablas creadas, Serian exclusivas para trabajo con el admin.
* Siempre realizar estos 2 pasos de migracion para no romper la cargar.
## 10. Creamos los datos del user y admin ##
    --> python manage.py createsuperuser
* Esto nos permite crear sus datos:
* Username (leave blank to use 'svera'): admin <-- usamos admin como username
* Email address: jona@gmail.com
* Password: 1234
* Password (again): 1234 <-- tener en cuenta que no es visible
* This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

## Pobramos de nuevo ejecutando ##
    --> python manage.py runserver
* runserver y abrimos la app
* http://127.0.0.1:8000/admin/ 
* escribimos en la ruta /admin y nos permite logearlos
con el usuario y clave.
* dentro de la web podemos crear usarios, administrarlos, etc

## Tenemos que tener creado la viriable de entorno dentro del proyecto, por buenas practicas, este se crea entre las carpetas seria el --> .env <--, nos sirve para guardar claves y usuarios.

## 11. Creamos una app llamda web ##
    --> python manage.py startapp web
* Al tenerla creada esta contiene varios archivos.py, como buena practica dentro de la app
tenemos que tener la carpeta templates y dentro un index.html, tambien una carpeta static que contiene
css dentro style.css, js dentro index.js y una img.
* Todo esto debemos conectarlos para que funcione

## Ejecutamos el proyecto para mandar un mensaje ##
    --> python manage.py runserver
* Dentro de la aplicacion web en --> views.py <--, crearemos funciones que nos devolvera mensajes.
* Debemos añadir lo siguiente para obtener una respuesta de hhtp y una de json
--> from django.http import HttpResponse, JsonResponse
* Aparte --> render -> templates
         --> HttpResponse -> text
         --> JsonResponse -> json
* La funcion que esta en el view del template debemos añadir la respuesta en index.html

## 12. Importamos las funciones al proyecto onlyflans en el archivo urls.py ##
* importamos funciones creadas (sin modularizacion):
from web.views import hola_text, hola_json, hola_template
* Creamos rutas de respuestas para cada funcion
* urlpatterns = [
    path('admin/', admin.site.urls),
    path('text/', hola_text),
    path('json/',  hola_json),
    path('template/', hola_template),
]
## 13. Debemos añadir nuestra app a settings.py del proyecto ##
* Donde dice definicion de aplicaciones debemos añadir 'web' que seria nuestra app, 
sino no podremos manejar los modelos y los templates

## Probamos los mensajes de las funciones:
* http://127.0.0.1:8000/text/
* http://127.0.0.1:8000/json/
* http://127.0.0.1:8000/template/

## ----------------------------------------------- ##
## Para Modularizar Routes en URLS (usar siempre) ##
* Creamos el archivo url.py dentro de nuestra app, importamos views.py, seria
la mejor forma de crear las route.
* Probamos nuestra web
* salimos del entorno y proyecto con el comando
    --> deactivate

## Pendiente practicar La modularizacion de routes ##
## Integrantes 
--> Jonathan Vera