# Hito 3
# Inicializamos el entorno y ejecutamos el server
```py
source venv/Scripts/activate
python manage.py runserver
```
# Creamos el modelo flan, migramos y creamos el SuperUser
```py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
<!-- Antes de abrir el server debemos importar Flan a admin.py, sino no se vera reflejado Flan. -->
# Añadimos 8 flanes 
- ingresamos como admin y añadimos 8 flanes con sus datos.
- En la views.py hacemos un llamado de todos los flanes.
- En el index.html creamos un codigo para crear unas cards donde mostrara la imagen, descripcion, precio y stock y le hacemos un estilo.
# Modificamos la vistas de index (indice) y welcome (bienvenido)
- Realizamos un filtrado para traer los flanes publicos y privados y los renderizamos en los templates.

# Creamos el Modelo ContacForm
- creamos el modelo y realizamos las migraciones e importamos el modelo al admin.py
- Realizamos una vista y agregamos la url, creamos el contact.html y añadimos la url al nabvar

# Form.py
- Creamos el forms.py y añadimos la clase contactformform

# Creamos la vista contact y success
- creamos la vista contact con el post para que valide el mensaje y creamos una vista simple de success
- Añadimos las url contacto y success
- creamos el success.html para cuando el mensaje sea exitoso
- verificamos los mensajes en el /admin

```py

```
