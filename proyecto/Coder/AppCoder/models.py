from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Guitarra(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
class Baterias(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
class Microfonos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField()  
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
class Bajos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    