from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from AppCoder.forms import GuitarraFormulario,BajoFormulario,MicrofonoFormulario,BateriaFormulario
from AppCoder.models import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView

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

@login_required
def crear_guitarra(request):
   if request.method == "POST":
       formulario = GuitarraFormulario(request.POST)
       
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           precio = data["precio"]
           descripcion = data["descripcion"]
           disponibilidad = data["disponibilidad"]
           creador = request.user
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

@login_required
def crear_bajo(request):
   if request.method == "POST":
       formulario = BajoFormulario(request.POST)
       
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           precio = data["precio"]
           descripcion = data["descripcion"]
           disponibilidad = data["disponibilidad"]
           creador = request.user
           bajo = Bajos(nombre=nombre, precio=precio,descripcion=descripcion,disponibilidad=disponibilidad)  # lo crean solo en RAM
           bajo.save()  # Lo guardan en la Base de datos

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

@login_required
def crear_microfono(request):
   if request.method == "POST":
       formulario = MicrofonoFormulario(request.POST)
       
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           precio = data["precio"]
           descripcion = data["descripcion"]
           disponibilidad = data["disponibilidad"]
           creador = request.user
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

@login_required
def crear_bateria(request):
   if request.method == "POST":
       formulario = BateriaFormulario(request.POST)
       
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           precio = data["precio"]
           descripcion = data["descripcion"]
           disponibilidad = data["disponibilidad"]
           creador = request.user
           bateria = Baterias(nombre=nombre, precio=precio,descripcion=descripcion,disponibilidad=disponibilidad)  # lo crean solo en RAM
           bateria.save()  # Lo guardan en la Base de datos

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

def buscar_bajo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        bajos = Bajos.objects.filter(nombre__contains=busqueda)
        contexto = {
            "bajos": bajos,
        }
        http_response = render(
            request=request,
            template_name='AppCoder/lista_bajos.html',
            context=contexto,
        )
        return http_response
    
def buscar_microfono(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        microfonos = Microfonos.objects.filter(nombre__contains=busqueda)
        contexto = {
            "microfonos": microfonos,
        }
        http_response = render(
            request=request,
            template_name='AppCoder/lista_microfonos.html',
            context=contexto,
        )
        return http_response
def buscar_bateria(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        baterias = Baterias.objects.filter(nombre__contains=busqueda)
        contexto = {
            "baterias": baterias,
        }
        http_response = render(
            request=request,
            template_name='AppCoder/lista_baterias.html',
            context=contexto,
        )
        return http_response
    
def listar_guitarras(request):
   contexto = {
       "guitarras": Guitarra.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='AppCoder/lista_guitarras.html',
       context=contexto,
   )
   return http_response

def listar_bajos(request):
   contexto = {
       "bajos": Bajos.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='AppCoder/lista_bajos.html',
       context=contexto,
   )
   return http_response


def listar_microfonos(request):
   contexto = {
       "microfonos": Microfonos.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='AppCoder/lista_microfonos.html',
       context=contexto,
   )
   return http_response

def listar_baterias(request):
   contexto = {
       "baterias": Baterias.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='AppCoder/lista_baterias.html',
       context=contexto,
   )
   return http_response

def eliminar_guitarra(request, id):
   guitarra = Guitarra.objects.get(id=id)
   if request.method == "GET":
       guitarra.delete()
       url_exitosa = reverse('lista_guitarras')
       return redirect(url_exitosa)
   
def eliminar_bajo(request, id):
   bajo = Bajos.objects.get(id=id)
   if request.method == "GET":
       bajo.delete()
       url_exitosa = reverse('lista_bajos')
       return redirect(url_exitosa)
   
def eliminar_microfono(request, id):
   microfono = Microfonos.objects.get(id=id)
   if request.method == "GET":
       microfono.delete()
       url_exitosa = reverse('lista_microfonos')
       return redirect(url_exitosa)
   
def eliminar_bateria(request, id):
   bateria = Baterias.objects.get(id=id)
   if request.method == "GET":
       bateria.delete()
       url_exitosa = reverse('lista_baterias')
       return redirect(url_exitosa)
   
def editar_guitarra(request, id):
   guitarra = Guitarra.objects.get(id=id)
   if request.method == "POST":
       formulario = GuitarraFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           guitarra.nombre = data['nombre']
           guitarra.precio = data['precio']
           guitarra.descripcion = data['descripcion']
           guitarra.save()
           url_exitosa = reverse('lista_guitarras')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': guitarra.nombre,
           'precio': guitarra.precio,
           'descripcion':guitarra.descripcion,
       }
       formulario = GuitarraFormulario(initial=inicial)
   return render(
       request=request,
       template_name='AppCoder/formulario_guitarra.html',
       context={'formulario': formulario},
   )
   
def editar_bajo(request, id):
   bajo = Bajos.objects.get(id=id)
   if request.method == "POST":
       formulario = BajoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           bajo.nombre = data['nombre']
           bajo.precio = data['precio']
           bajo.descripcion = data['descripcion']
           bajo.save()
           url_exitosa = reverse('lista_bajos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': bajo.nombre,
           'precio': bajo.precio,
           'descripcion': bajo.descripcion,
       }
       formulario = GuitarraFormulario(initial=inicial)
   return render(
       request=request,
       template_name='AppCoder/formulario_bajo.html',
       context={'formulario': formulario},
   )
def editar_microfono(request, id):
   microfono = Microfonos.objects.get(id=id)
   if request.method == "POST":
       formulario = MicrofonoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           microfono.nombre = data['nombre']
           microfono.precio = data['precio']
           microfono.descripcion = data['descripcion']
           microfono.save()
           url_exitosa = reverse('lista_microfonos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': microfono.nombre,
           'precio': microfono.precio,
           'descripcion': microfono.descripcion,
       }
       formulario = MicrofonoFormulario(initial=inicial)
   return render(
       request=request,
       template_name='AppCoder/formulario_microfono.html',
       context={'formulario': formulario},
   )
def editar_bateria(request, id):
   bateria = Baterias.objects.get(id=id)
   if request.method == "POST":
       formulario = BateriaFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           bateria.nombre = data['nombre']
           bateria.precio = data['precio']
           bateria.descripcion = data['descripcion']
           bateria.save()
           url_exitosa = reverse('lista_baterias')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': bateria.nombre,
           'precio': bateria.precio,
           'descripcion': bateria.descripcion,
       }
       formulario = BateriaFormulario(initial=inicial)
   return render(
       request=request,
       template_name='AppCoder/formulario_bateria.html',
       context={'formulario': formulario},
   )
class GuitarraListView(ListView):
   model = Guitarra
   template_name = 'AppCoder/lista_guitarras.html'

class BajoListView(ListView):
   model = Bajos
   template_name = 'AppCoder/lista_bajos.html'

class BateriaListView(ListView):
   model = Baterias
   template_name = 'AppCoder/lista_baterias.html'

class MicrofonoListView(ListView):
   model = Microfonos
   template_name = 'AppCoder/lista_microfonos.html'

class GuitarraDetailView(DetailView):
   model = Guitarra
   success_url = reverse_lazy('lista_guitarras')
   
class BajoDetailView(DetailView):
   model = Bajos
   success_url = reverse_lazy('lista_bajos')

class BateriaDetailView(DetailView):
   model = Baterias
   success_url = reverse_lazy('lista_baterias')

class MicrofonoDetailView(DetailView):
   model = Microfonos
   success_url = reverse_lazy('lista_microfonos')

class GuitarraCreateView(CreateView):
   model = Guitarra
   fields = ('Nombre', 'Precio', 'Descripcion', 'Disponibilidiad')
   success_url = reverse_lazy('lista_guitarras')

class BajoCreateView(CreateView):
   model = Bajos
   fields = ('Nombre', 'Precio', 'Descripcion', 'Disponibilidiad')
   success_url = reverse_lazy('lista_bajos')

class BateriaCreateView(CreateView):
   model = Baterias
   fields = ('Nombre', 'Precio', 'Descripcion', 'Disponibilidiad')
   success_url = reverse_lazy('lista_baterias')

class MicrofonoCreateView(CreateView):
   model = Microfonos
   fields = ('Nombre', 'Precio', 'Descripcion', 'Disponibilidiad')
   success_url = reverse_lazy('lista_microfonos')

class GuitarraUpdateView(UpdateView):
   model = Guitarra
   fields = ('Nombre', 'Precio', 'Descripcion', 'Disponibilidiad')
   success_url = reverse_lazy('lista_guitarras')

class BajoUpdateView(UpdateView):
   model = Bajos
   fields = ('Nombre', 'Precio', 'Descripcion', 'Disponibilidiad')
   success_url = reverse_lazy('lista_bajos')

class BateriaUpdateView(UpdateView):
   model = Baterias
   fields = ('Nombre', 'Precio', 'Descripcion', 'Disponibilidiad')
   success_url = reverse_lazy('lista_baterias')

class MicrofonoUpdateView(UpdateView):
   model = Microfonos
   fields = ('Nombre', 'Precio', 'Descripcion', 'Disponibilidiad')
   success_url = reverse_lazy('lista_microfonos')

class GuitarraDeleteView(DeleteView):
   model = Guitarra
   success_url = reverse_lazy('lista_guitarras')

class BajoDeleteView(DeleteView):
   model = Bajos
   success_url = reverse_lazy('lista_bajos')

class BateriaDeleteView(DeleteView):
   model = Baterias
   success_url = reverse_lazy('lista_baterias')

class MicrofonoDeleteView(DeleteView):
   model = Microfonos
   success_url = reverse_lazy('lista_microfonos')