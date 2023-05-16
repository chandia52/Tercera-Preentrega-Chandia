from django.urls import path 
from django.contrib import admin

from AppCoder.views import listar_guitarras, listar_bajos,listar_baterias,listar_microfonos,crear_guitarra,crear_bajo,crear_microfono,crear_bateria,buscar_guitarra

urlpatterns = [
    path("guitarras/", listar_guitarras, name="lista_guitarras"),
    path("bajos/", listar_bajos,name="lista_bajos"),
    path("baterias/",listar_baterias,name="lista_baterias"),
    path("microfonos/",listar_microfonos,name="lista_microfonos"),
    path("crear-guitarra/",crear_guitarra, name="crear_guitarra"),
    path("crear-bajo/",crear_bajo, name="crear_bajo"),
    path("crear-microfono/",crear_microfono, name="crear_microfono"),
    path("crear-bateria/",crear_bateria, name="crear_bateria"),
    path("buscar-guitarra/", buscar_guitarra, name="buscar_guitarra"),
    
]
