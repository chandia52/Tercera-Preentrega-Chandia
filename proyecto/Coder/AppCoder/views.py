from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from AppCoder.forms import GuitarraFormulario,BajoFormulario,MicrofonoFormulario,BateriaFormulario
from AppCoder.models import Guitarra,Bajos,Microfonos,Baterias
from django.http import HttpResponse
# Create your views here.

def listar_guitarras(request):
    contexto = {
        "guitarras": Guitarra.objects.all()
    }
    http_response = render(
        request=request,
        template_name='AppCoder/lista_guitarras.html',
        context=contexto,
    )
    return http_response


def listar_bajos(request):
    contexto = {
       "bajos": Bajos.objects.all()
    }
    http_response = render(
        request=request,
        template_name='AppCoder/lista_bajos.html',
        context=contexto,
    )
    return http_response

def listar_baterias(request):
    contexto = {
       "baterias": Baterias.objects.all()
    }
    http_response = render(
        request=request,
        template_name='AppCoder/lista_baterias.html',
        context=contexto,
    )
    return http_response
def listar_microfonos(request):
    contexto = {
        "microfonos" : Microfonos.objects.all()
       }
    http_response = render(
        request=request,
        template_name='AppCoder/lista_microfonos.html',
        context=contexto,
    )
    return http_response

def crear_guitarra(request):
   if request.method == "POST":
       formulario = GuitarraFormulario(request.POST)
       
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           precio = data["precio"]
           descripcion = data["descripcion"]
           disponibilidad = data["disponibilidad"]
           guitarra = Guitarra(nombre=nombre, precio=precio,descripcion=descripcion,disponibilidad=disponibilidad)  # lo crean solo en RAM
           guitarra.save()  # Lo guardan en la Base de datos

           # Redirecciono al guitarra a la lista de guitarras
           url_exitosa = reverse('lista_guitarras')  # instrumentos/guitarras/
           return redirect(url_exitosa)
   else:  # GET
       formulario = GuitarraFormulario()
   http_response = render(
       request=request,
       template_name='AppCoder/formulario_guitarra.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_bajo(request):
   if request.method == "POST":
       formulario = BajoFormulario(request.POST)
       
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           precio = data["precio"]
           descripcion = data["descripcion"]
           disponibilidad = data["disponibilidad"]
           guitarra = Bajos(nombre=nombre, precio=precio,descripcion=descripcion,disponibilidad=disponibilidad)  # lo crean solo en RAM
           guitarra.save()  # Lo guardan en la Base de datos

           # Redirecciono al guitarra a la lista de bajos
           url_exitosa = reverse('lista_bajos')  # instrumentos/bajos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = BajoFormulario()
   http_response = render(
       request=request,
       template_name='AppCoder/formulario_bajo.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_microfono(request):
   if request.method == "POST":
       formulario = MicrofonoFormulario(request.POST)
       
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           precio = data["precio"]
           descripcion = data["descripcion"]
           disponibilidad = data["disponibilidad"]
           microfono = Microfonos(nombre=nombre, precio=precio,descripcion=descripcion,disponibilidad=disponibilidad)  # lo crean solo en RAM
           microfono.save()  # Lo guardan en la Base de datos

           # Redirecciono al guitarra a la lista de microfonos
           url_exitosa = reverse('lista_microfonos')  # instrumentos/microfonos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = MicrofonoFormulario()
   http_response = render(
       request=request,
       template_name='AppCoder/formulario_microfono.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_bateria(request):
   if request.method == "POST":
       formulario = BateriaFormulario(request.POST)
       
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           precio = data["precio"]
           descripcion = data["descripcion"]
           disponibilidad = data["disponibilidad"]
           guitarra = Baterias(nombre=nombre, precio=precio,descripcion=descripcion,disponibilidad=disponibilidad)  # lo crean solo en RAM
           guitarra.save()  # Lo guardan en la Base de datos

           # Redirecciono al guitarra a la lista de bateria
           url_exitosa = reverse('lista_baterias')  # instrumentos/bateria/
           return redirect(url_exitosa)
   else:  # GET
       formulario = BateriaFormulario()
   http_response = render(
       request=request,
       template_name='AppCoder/formulario_bateria.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_guitarra(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        guitarras = Guitarra.objects.filter(nombre__contains=busqueda)
        contexto = {
            "guitarras": guitarras,
        }
        http_response = render(
            request=request,
            template_name='AppCoder/lista_guitarras.html',
            context=contexto,
        )
        return http_response