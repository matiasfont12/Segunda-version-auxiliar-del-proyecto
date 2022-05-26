from django.shortcuts import redirect, render
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import FormularioUser, EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension


def login(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user=user)
                return render(request,"accounts/index.html",{"msj": "Te logeaste"})
            
            else:
                return render(request,"accounts/login.html", {"form": form, "msj": "No se autentico"})
        else:
            return render(request,"accounts/login.html", {"form": form, "msj": "Datos con formato incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request,"accounts/login.html", {"form": form, "msj":""})
    
    
def register(request):
    
    if request.method == "POST":
        form = FormularioUser(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            
            form.save()
            return render(request,"accounts/index.html", {"msj": "Se creo el usuario"})
        else:
            return render(request,"accounts/register.html", {"form": form, "msj": ""})
        
        
    form = FormularioUser()
    return render(request, "accounts/register.html", {"form": form, "msj": ""})

@login_required
def editar(request):
    
    user_extension_logued = UserExtension.objects.get_or_create(user=request.user)
    
    
    if request.method == "POST":
        form = EditFullUser(request.POST)
        
        if form.is_valid():
            request.user.email = form.cleaned_data["username"]
            request.user.first_name= form.cleaned_data["first_name"]
            request.user.last_name = form.cleaned_data["last_name"]
            user_extension_logued.avatar = form.cleaned_data["avatar"]
            user_extension_logued.link = form.cleaned_data["link"]
            user_extension_logued.more_description = form.cleaned_data["more_description"]
            
            if form.cleaned_data["password1"] != "" and form.cleaned_data["password1"] == form.cleaned_data["password2"]:
                request.user.set_password("password1")
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect("index")
        else:
            return render(request,"accounts/edit_user.html", {"form": form, "msj": "Form is not valid..."})
        
    form = EditFullUser(
        initial={ 
        "email" : request.user.email,
        "password1": "" ,
        "password2": "",
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "avatar": user_extension_logued.avatar,
        "link": user_extension_logued.link,
        "more_description": user_extension_logued.more_description
            
        }
    )
    return render(request, "accounts/edit_user.html", {"form": form})

    
    