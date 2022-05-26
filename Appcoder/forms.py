from django import forms
from ckeditor.fields import RichTextFormField


class CursoFormulario(forms.Form):
  nombre = forms.CharField(max_length=20)
  curso = forms.IntegerField()
  # tarjeta_presentacion = RichTextFormField(required=False)
  
class BusquedaNombre(forms.Form):
  nombre = forms.CharField(max_length=20)
  
class EstudianteFormulario(forms.Form):
  
  nombre= forms.CharField(max_length=30)
  apellido= forms.CharField(max_length=20)
  email = forms.EmailField()
  tarjeta_presentacion = RichTextFormField(required=False)
  
  
  