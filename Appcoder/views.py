from django.http import HttpResponse
from django.shortcuts import render, redirect
from Appcoder.models import Curso, Estudiante, Profesor
from Appcoder.forms import CursoFormulario, BusquedaNombre, EstudianteFormulario
import random
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def nuevo_curso(request):
    curso = random.randrange(1500,3000)
    nuevo_curso = Curso(nombre = "Curso Python", curso=curso)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} {nuevo_curso.curso}")

def formulario_curso(request):
  
  formulario = CursoFormulario() #Hacemos llamado del form y lo guardamos en una variable para trabajarlo
  
  if request.method == "POST": # La información del formulario siempre entrara por el metodo post
    formulario = CursoFormulario(request.POST) #Entonces, si esto es asi, que la información ingrese y se muestre
    print(request.POST)
    
  if formulario.is_valid():#Si al ingresar, la informacion es valida:
    data = formulario.cleaned_data #Que se guarde
    nuevo_curso = Curso(nombre=data["nombre"], curso=data["curso"])#Al guardarse, construimos con ella llamando al modelo
    nuevo_curso.save()#Guardamos la informacion
    
    return render(request,"Appcoder/formulario.html",{"nuevo_curso":nuevo_curso})#Entregamos la informacion 
    
  else: 
   formulario = CursoFormulario()
   return render(request,"Appcoder/formulario.html",{"formulario":formulario})
  
def busqueda_nombre(request):
  
  nombre_buscado = []
  
  dato = request.GET.get("nombre", None)
  if dato is not None:
    nombre_buscado = Curso.objects.filter(nombre__icontains=dato)

  busqueda = BusquedaNombre()
  

  return render(request,"Appcoder/busqueda_nombre.html",
                {"busqueda": busqueda, 
                 "nombre_buscado": nombre_buscado,
                 "dato": dato})
  
def listado_estudiantes(request):
  
  listado_estudiantes = Estudiante.objects.all()
  
  return render(request,"Appcoder/listado_estudiantes.html",
                {"listado_estudiantes": listado_estudiantes})  
  
  
@login_required 
def crear_estudiante(request):
  
  formulario = EstudianteFormulario()
  
  if request.method == "POST":
    formulario = EstudianteFormulario(request.POST)
    print(request.POST)
    
  if formulario.is_valid():
    data = formulario.cleaned_data
    nuevo_estudiante = Estudiante(
      
      nombre=data["nombre"],
      apellido=data["apellido"],
      email=data["email"],
      tarjeta_presentacion=data["tarjeta_presentacion"]
      )
    
    nuevo_estudiante.save()
    
    return redirect("listado_estudiantes")
  
  else:
   formulario = EstudianteFormulario()

   return render(
     request,"Appcoder/crear_estudiante.html",
     {"formulario":formulario}
     )

def actualizar_estudiante(request, id):
  
  estudiante = Estudiante.objects.get(id=id)
  
  formulario = EstudianteFormulario()
  
  if request.method == "POST":
    formulario = EstudianteFormulario(request.POST)
    print(request.POST)
    
  if formulario.is_valid():
    data = formulario.cleaned_data
    estudiante.nombre = data["nombre"]
    estudiante.apellido = data["apellido"]
    estudiante.email = data["email"]
    estudiante.save()
    
    return redirect("listado_estudiantes")
  
  else:
   formulario = EstudianteFormulario(
     initial={
       "nombre": estudiante.nombre,
       "apellido": estudiante.apellido,
       "email": estudiante.email
     }
   )

   return render(
     request,"Appcoder/actualizar_estudiante.html",
     {"formulario":formulario,
      "estudiante": estudiante
      }
    )

def borrar_estudiante(request,id):
  estudiante = Estudiante.objects.get(id=id)
  estudiante.delete()
   
  return redirect("listado_estudiantes")
  

class ProfesorLista(ListView):
  model = Profesor
  template_name = "Appcoder/profesor_list.html"
  
  
class ProfesorDetalle(DetailView):
  model = Profesor
  template_name = "Appcoder/profesor_datos.html"
  
class ProfesorCrear(LoginRequiredMixin, CreateView):
  model = Profesor
  success_url = "/Appcoder/profesores/"
  fields = ["nombre", "apellido", "email", "profesion", "informacion", "tiempo_de_creacion"]
  
  
class ProfesorEditar(LoginRequiredMixin, UpdateView):
  model = Profesor
  success_url = "/Appcoder/profesores/"
  fields = ["nombre", "apellido", "email", "informacion", "tiempo_de_creacion"]
  
  
class ProfesorBorrar(LoginRequiredMixin, DeleteView):
  model = Profesor
  success_url = "/Appcoder/profesores/"