from django.urls import path
from .views import inicio, mi_plantilla, otra_vista, login, register, editar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("plantilla/", mi_plantilla, name= "plantilla"),
    path("otravista/",otra_vista, name= "otra_vista"), 
    path("login/", login,name= "login"),
    path("logout/", LogoutView.as_view(template_name="Indice/logout.html"), name="logout"),
    path("register/", register, name= "register"),
    path("editar/", editar, name= "editar")
]