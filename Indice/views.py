from django.http import HttpResponse 
import random
from django.shortcuts import render

def inicio(request):
    return render(request, "Indice/index.html", {})

def otra_vista(request):
    return HttpResponse(
"<h1>Su privacidad es importante para nosotros. Para protejer mejor su privacidad proporcionamos este aviso que explica nuestras practicas de informacion en linea y sobre la manera que se recoje y se utiliza su informacion.<h1>")

def numero_random(request):
    numero = random.randrange(15,180)
    return HttpResponse        

def mi_plantilla(request):
  
    nombre = "matias emanuel"
    apellido = "font"
    lista = [1,2,3,4,5]
    
    diccionario_de_datos = {
     "nombre": nombre,
     "apellido": apellido,
     "lista": lista
    }
    
    return render(request, "Indice/plantillas.html", diccionario_de_datos)
  
    
    