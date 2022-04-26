from django.http import HttpResponse 
import random
from django.shortcuts import redirect, render
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import FormularioUser, EdicionUser
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "Indice/index.html", {})


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


def login(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user=user)
                return render(request,"Indice/index.html",{"msj": "Te logeaste"})
            
            else:
                return render(request,"Indice/login.html", {"form": form, "msj": "No se autentico"})
        else:
            return render(request,"Indice/login.html", {"form": form, "msj": "Datos con formato incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request,"Indice/login.html", {"form": form, "msj":""})
    
    
def register(request):
    
    if request.method == "POST":
        form = FormularioUser(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            
            form.save()
            return render("Indice/index.html", {"msj": "Se creo el usuario"})
        else:
            return render("Indice/register.html", {"form": form, "msj": ""})
        
        
    form = FormularioUser()
    return render(request, "Indice/register.html", {"form": form, "msj": ""})


@login_required
def editar(request):
    
    request.user
    
    
    
    if request.method == "POST":
        form = EdicionUser(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            request.user.first_name = data.get("first_name", "")
            request.user.last_name = data.get("last_name", "")
            request.user.email = data.get("email", "")
            if data.get("password1") == data.get("password2") and len(data.get("password1")) < 8:
                request.user.set_password(data.get("password1"))
            
            request.user.save()
            return render("Indice/index.html", {"msj": ""})
        else:
            return render("Indice/editar_user.html", {"form": form, "msj": ""})
        
        
    form = EdicionUser(
        initial={
       "first_name": request.user.first_name,
       "last_name": request.user.last_name,
       "email": request.user.email,
       "username": request.user.username
     }
    )
    return render(request, "Indice/editar_user.html", {"form": form, "msj": ""})
