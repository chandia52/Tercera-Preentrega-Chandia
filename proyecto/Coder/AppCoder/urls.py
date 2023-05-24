from django.urls import path 
from django.contrib import admin

from AppCoder.views import listar_guitarras, listar_bajos,listar_baterias,listar_microfonos,\
    crear_guitarra,crear_bajo,crear_microfono,crear_bateria,buscar_guitarra,\
    eliminar_bajo,eliminar_bateria,eliminar_guitarra,eliminar_microfono, editar_bajo, editar_bateria,editar_guitarra,\
    editar_microfono,GuitarraCreateView,GuitarraDeleteView,GuitarraDetailView,GuitarraListView,GuitarraUpdateView,\
    BateriaCreateView,BateriaDeleteView,BateriaDetailView,BateriaListView,BateriaUpdateView,\
    MicrofonoCreateView,MicrofonoDeleteView,MicrofonoDetailView,MicrofonoListView,MicrofonoUpdateView,\
    BajoCreateView,BajoDeleteView,BajoDetailView,BajoListView,BajoUpdateView,buscar_bajo,buscar_bateria,buscar_microfono

    


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
    path("buscar-bajo/", buscar_bajo, name="buscar_bajo"),
    path("buscar-microfono/", buscar_microfono, name="buscar_microfono"),
    path("buscar-bateria/", buscar_bateria, name="buscar_bateria"),
    path('eliminar-guitarra/<int:id>/', eliminar_guitarra, name="eliminar_guitarra"),
    path('eliminar-bajo/<int:id>/', eliminar_bajo, name="eliminar_bajo"),
    path('eliminar-microfono/<int:id>/', eliminar_microfono, name="eliminar_microfono"),
    path('eliminar-bateria/<int:id>/', eliminar_bateria, name="eliminar_bateria"),
    path('editar-guitarra/<int:id>/', editar_guitarra, name="editar_guitarra"),
    path('editar-bajo/<int:id>/', editar_bajo, name="editar_bajo"),
    path('editar-microfono/<int:id>/', editar_microfono, name="editar_microfono"),
    path('editar-bateria/<int:id>/', editar_bateria, name="editar_bateria"),
    #URLS CRUD
    path("guitarras/", GuitarraListView.as_view(), name="lista_guitarras"),
    path('guitarras/<int:pk>/', GuitarraDetailView.as_view(), name="ver_guitarra"),
    path('crear-guitarra/', GuitarraCreateView.as_view(), name="crear_guitarra"),
    path('editar-guitarra/<int:pk>/', GuitarraUpdateView.as_view(), name="editar_guitarra"),
    path('eliminar-guitarra/<int:pk>/', GuitarraDeleteView.as_view(), name="eliminar_guitarra"),
    path("bajos/", BajoListView.as_view(), name="lista_bajos"),
    path('bajos/<int:pk>/', BajoDetailView.as_view(), name="ver_bajo"),
    path('crear-bajo/', BajoCreateView.as_view(), name="crear_bajo"),
    path('editar-bajo/<int:pk>/', BajoUpdateView.as_view(), name="editar_bajo"),
    path('eliminar-bajo/<int:pk>/', BajoDeleteView.as_view(), name="eliminar_bajo"),
    path("baterias/", BateriaListView.as_view(), name="lista_baterias"),
    path('baterias/<int:pk>/', BateriaDetailView.as_view(), name="ver_bateria"),
    path('crear-bateria/', BateriaCreateView.as_view(), name="crear_bateria"),
    path('editar-bateria/<int:pk>/', BateriaUpdateView.as_view(), name="editar_bateria"),
    path('eliminar-bateria/<int:pk>/', BateriaDeleteView.as_view(), name="eliminar_bateria"),
    path("microfonos/", MicrofonoListView.as_view(), name="lista_microfonos"),
    path('microfonos/<int:pk>/', MicrofonoDetailView.as_view(), name="ver_microfono"),
    path('crear-microfono/', MicrofonoCreateView.as_view(), name="crear_microfono"),
    path('editar-microfono/<int:pk>/', MicrofonoUpdateView.as_view(), name="editar_microfono"),
    path('eliminar-microfono/<int:pk>/', MicrofonoDeleteView.as_view(), name="eliminar_microfono"),
]
  
    

