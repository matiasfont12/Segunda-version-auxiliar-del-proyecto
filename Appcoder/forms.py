from django import forms

class CursoFormulario(forms.Form):
  nombre = forms.CharField(max_length=20)
  curso = forms.IntegerField()
  
class BusquedaNombre(forms.Form):
  nombre = forms.CharField(max_length=20)
  
class EstudianteFormulario(forms.Form):
  
  nombre= forms.CharField(max_length=30)
  apellido= forms.CharField(max_length=20)
  email = forms.EmailField()
  
  