from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("plantilla/", views.mi_plantilla, name= "plantilla"),
    path("about/", views.about, name= "about"), 
    path("login/", views.login,name= "login"),
    path("logout/", LogoutView.as_view(template_name="Indice/logout.html"), name="logout"),
    path("register/", views.register, name= "register"),
    path("editar/", views.editar, name= "editar")
]