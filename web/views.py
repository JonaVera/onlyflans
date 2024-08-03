from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def hola(req):
    return HttpResponse("SOLO MODIFIQUE EL HTML DIRIJASE AL /TEMPLATE EN LA URL")

def hola_text(req):
    return HttpResponse("Bienvenido a OnlyFlans")

def hola_json(req):
    data = {
        "mensaje": "Probando Json"
    }
    return JsonResponse(data)

# Este requiere tres objetos para ejecutar el return   
def hola_template(req):
    context = {
        "mensaje": "Tenemos una gran variedad de flan"
    }
    return render(req, 'index.html', context)
    
# --> render -> templates
# --> HttpResponse -> text
# --> JsonResponse -> json