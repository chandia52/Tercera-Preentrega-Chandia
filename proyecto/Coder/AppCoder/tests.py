from django.test import TestCase

from django.db import IntegrityError
from AppCoder.models import Guitarra,Microfonos,Bajos,Baterias
# Create your tests here.

class GuitarraTests(TestCase):
   """Aqui realizamos todas las pruebas en el modelo guitarra."""

   def test_creacion_guitarra(self):
       # caso uso esperado
       guitarra = Guitarra(nombre="Stratocaster",precio=452000,descripcion="Bonita guitarra",disponibilidad=True)
       guitarra.save()

       # Compruebo que la guitarra fue creada y la data fue guardada correctamente
       self.assertEqual(Guitarra.objects.count(), 1)
       self.assertEqual(guitarra.nombre, "Stratocaster")
       self.assertEqual(guitarra.precio, 452000)
       self.assertEqual(guitarra.descripcion, "Bonita guitarra")
       self.assertEqual(guitarra.disponibilidad, True)
   def test_guitarra_str(self):
       guitarra = Guitarra(nombre="Gibson", precio=472000,descripcion="Bonita pastilla",disponibilidad= True)
       guitarra.save()

class BajosTests(TestCase):
   """Aqui realizamos todas las pruebas en el modelo bajos."""

   def test_creacion_bajos(self):
       # caso uso esperado
       bajo = Bajos(nombre="JazzBass",precio=100000,descripcion="Bonita pastilla",disponibilidad=True)
       bajo.save()

       # Compruebo que el bajo fue creado y la data fue guardado correctamente
       self.assertEqual(Bajos.objects.count(), 1)
       self.assertEqual(bajo.nombre, "JazzBass")
       self.assertEqual(bajo.precio, 100000)
       self.assertEqual(bajo.descripcion, "Bonita pastilla")
       self.assertEqual(bajo.disponibilidad, True)
   def test_bajos_str(self):
       bajo = Bajos(nombre="Funky", precio=20000,descripcion="Economico",disponibilidad= True)
       bajo.save()

       
class MicrofonosTests(TestCase):
   """Aqui realizamos todas las pruebas en el modelo microfonos."""

   def test_creacion_microfonos(self):
       # caso uso esperado
       microfono = Microfonos(nombre="Senheiser",precio=15000,descripcion="Bonito diseño",disponibilidad=True)
       microfono.save()

       # Compruebo que el microfono fue creado y la data fue guardado correctamente
       self.assertEqual(Microfonos.objects.count(), 1)
       self.assertEqual(microfono.nombre, "Senheiser")
       self.assertEqual(microfono.precio, 15000)
       self.assertEqual(microfono.descripcion, "Bonito diseño")
       self.assertEqual(microfono.disponibilidad, True)
   def test_microfonos_str(self):
       microfono = Microfonos(nombre="Shure", precio=60000,descripcion="Buen sonido",disponibilidad= True)
       microfono.save()
    
class BateriasTests(TestCase):
   """Aqui realizamos todas las pruebas en el modelo baterias."""

   def test_creacion_baterias(self):
       # caso uso esperado
       bateria = Baterias(nombre="Mapex",precio=75000,descripcion="Buen sonido",disponibilidad=True)
       bateria.save()

       # Compruebo que la bateria fue creada y la data fue guardada correctamente
       self.assertEqual(Baterias.objects.count(), 1)
       self.assertEqual(bateria.nombre, "Mapex")
       self.assertEqual(bateria.precio, 75000)
       self.assertEqual(bateria.descripcion, "Buen sonido")
       self.assertEqual(bateria.disponibilidad, True)
   def test_baterias_str(self):
       bateria = Baterias(nombre="Eclair", precio=65000,descripcion="Economica",disponibilidad= True)
       bateria.save()