from django.db import models

# Create your models here.
class Guitarra(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField()
class Baterias(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField()
class Microfonos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField()  
class Bajos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField()
    
guitarra1 = Guitarra(nombre="Stratocaster Fender",precio=150000.00,descripcion="Vendo guitarra Fender Stratocaster, un clasico en guitarras.. Usadas por famosos como John Frusciante, excelente sonido, digna de ver.. Precio Charlable",disponibilidad=True)