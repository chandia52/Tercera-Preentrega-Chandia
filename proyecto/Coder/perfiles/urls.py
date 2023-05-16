from django.urls import path 
from django.contrib import admin
from perfiles.views import registro
from perfiles.views import registro, login_view,CustomLogoutView
urlpatterns = [
       # URLS Usuario y sesion
   path('registro/', registro, name="registro"),
   path('login/', login_view, name="login"),
   path('logout/', CustomLogoutView.as_view(), name="logout"),

    
]
