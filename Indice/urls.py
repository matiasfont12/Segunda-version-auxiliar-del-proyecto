from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("plantilla/", views.mi_plantilla, name= "plantilla"),
    path("about/", views.about, name= "about"), 
    
]