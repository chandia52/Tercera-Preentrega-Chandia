from django.http import HttpResponse
from django.shortcuts import render
 

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppCoder/index.html',
        context=contexto,
    )
    return http_response

def acerca_de_mi(request):
    contexto = {
        
    }
    http_response = render(
        request=request,
        template_name='AppCoder/about.html',
        context=contexto,
    )
    return http_response