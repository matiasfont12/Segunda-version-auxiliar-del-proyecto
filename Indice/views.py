from django.http import HttpResponse 
import random
from django.shortcuts import render
# from django.contrib.auth import login as django_login, authenticate
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# from .models import Avatar
# from ..accounts.forms import FormularioUser, EdicionUser
# from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "Indice/index.html", {})
    # return render(request, "Indice/index.html", {"user_avatar_url": buscar_url_avatar(request.user)})



def about(request):
    return render(request,"Indice/about.html", {})
   

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

