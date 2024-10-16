# Hito 5 
# Inicializamos el entorno y ejecutamos el server
```py
source venv/Scripts/activate
python manage.py runserver
```
# FUNCIONALIDAD EXTRA
# vista testimonio
- en welcome agregamos el boton Testimonio
- creamos el models testimonio
- migramos:
```py
python manage.py makemigrations
python manage.py migrate
```
- creamos la vista testimonio
- creamos el template testimonio.html
- agregamos la url

# formulario para testimonio
- Creamos el formulario testimonioform con sus campos e importamos el modelo.
- creamos la vista y con un post y validacion
- Creamos un template crear_testimonio.html
- agregamos la url

- añadimos testimonios con usuarios registrados