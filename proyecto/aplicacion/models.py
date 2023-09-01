from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} , {self.apellido}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    edad = models.IntegerField()

    class Meta:
        ordering = ['nombre']

    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Turno(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    dni = models.IntegerField(blank=False)
    fecha = models.DateField(blank=False)

    def __str__(self):
        return f"{self.nombre} , {self.dni} , {self.fecha}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    apellido = models.CharField(max_length=50)
    sueldo = models.IntegerField()
    trabajo = models.CharField(max_length=50)
    
    

