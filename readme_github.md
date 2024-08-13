## PASOS PARA SUBIR A GITHUB ##
## Primero verificar que estemos desconectados del entorno virtual ##
## 1. Inicializamos ## 
    --> git init
## 2. Creamos el repositorio en GITHUB ##
    --> Ponemos el mismo nombre del proyecto y lo dejamos publico
## 3. Copiamos el comando que nos da github ##
    --> git remote add origin https://github.com/JonaVera/onlyflans.git
## 4. Pegamos el comando en la terminal para conectarnos
## 5. Subimos la data
    --> git status
* Me muestra todo lo que hay que subir
    --> git add .
    --> git commit -m "init project onlyflans"
## 6. Subimos al repositorio (empuja todo)
    --> git push origin master

## Pasos para subir cambios ##
    --> git add .
    --> git commit -m "name" 
    --> git push origin master
