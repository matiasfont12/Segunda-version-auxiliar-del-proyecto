from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"
    


class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    nombre = models.CharField(max_length=10)
    curso = models.IntegerField()
    
    #Para hacer que el resultado que devuelva sea mas detallado, lo trabajamos en el modelo con un magicmethod __str__
    
    def __str__(self):
        
        
        return f"Usuario: {self.nombre}- Curso: {self.curso}"
#Lo bueno de esto es que para que el cambio se ejecute no hace falta hacer ni un makemigration ni un migration, ya que no estamos tocando en modelo


class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_de_entrega = models.DateTimeField()
    entregado = models.BooleanField()

  
