from django.contrib import admin

# Register your models here.

from .models import Curso, Profesor, Entregable, Estudiante

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Estudiante)

