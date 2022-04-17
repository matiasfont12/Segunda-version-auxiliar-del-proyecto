from django.urls import path
from .views import inicio, mi_plantilla, otra_vista

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("plantilla/", mi_plantilla, name= "plantilla"),
    path("otravista/",otra_vista, name= "otra_vista"), 
]