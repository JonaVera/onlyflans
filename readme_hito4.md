# Hito 4
# Inicializamos el entorno y ejecutamos el server
```py
source venv/Scripts/activate
python manage.py runserver
```
# Incluimos la url a nuestro sitio web
- Añadimos la url que contiene las rutas para login, logout, etc.

# Creamos la carpeta registrarion
- dentro de los templates tendremos las carpetas para el login y logout

# setting.py
- modificamos los redireccionamientos para iniciar sesion y cerrar sesion

# views.py 
- importamos los decoradores de seguiridad y lo agreagamos a la vista welcome.

# navbar 
- agregamos las etiquetas iniciar sesion y cerrar sesion
- configuramos la autenticacion

# index y welcome
- Modificamos cada uno añadiendo un codigo que muestre un texto y un boton.

# creamos 3 usuarios 
- ingresamos al sitio web (http://127.0.0.1:8000/admin/) e ingresamos sesion como administrador.
- creamos 3 usuarios:
    - username: Bruce 
    - password: brucebruce

    - username: Toto
    - password: totototo

    - username: Jack 
    - password: jack2007

- Ejecutamos y probamos las vistas con los usuarios