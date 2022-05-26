from django.urls import path
from . import views

urlpatterns = [
    path("nuevo/", views.nuevo_curso, name= "nuevo_curso"),
    path("curso/", views.formulario_curso, name= "formulario"),
    path("busqueda_nombre/", views.busqueda_nombre, name= "busqueda_nombre"),
    #CRUD FUNCTIONS: 
    # path("estudiante/", views.estudiante, name= "estudiante"),
    #CREATE:
    path("estudiante/crear", views.crear_estudiante, name= "crear_estudiante"),
    #READ:
    path("estudiante/listado", views.listado_estudiantes, name= "listado_estudiantes"),
    #UPDATE:
    path("estudiante/actualizar/<int:id>/", views.actualizar_estudiante, name= "actualizar_estudiante"),
    #DELETE:
    path("estudiante/borrar/<int:id>/", views.borrar_estudiante, name= "borrar_estudiante"),
    #Clases basadas en vistas
    path("profesores/", views.ProfesorLista.as_view(), name= "profesor_listado"),
    path("profesores/<int:pk>/", views.ProfesorDetalle.as_view(), name= "profesor_detalle"),
    path("profesores/crear", views.ProfesorCrear.as_view(), name="profesor_crear" ),
    path("profesores/<int:pk>/editar", views.ProfesorEditar.as_view(), name= "profesor_editar"),
    path("profesores/<int:pk>/borrar", views.ProfesorBorrar.as_view(), name= "profesor_borrar")
]
  
