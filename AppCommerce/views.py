from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'AppCommerce/index.html')


def register(request):
        if request.method == 'POST':
            try:
                usuario = Usuario.objects.get(email=request.POST['email'])
                return render(request, "AppCommerce/register.html", {"falla_usuario_existente":True})
            except:
                if request.POST['contrasenia'] == request.POST['contrasenia_verificacion']:
                    usuario = Usuario (nombre=request.POST['nombre'], contrasenia=request.POST['contrasenia'], email=request.POST['email'])
                    usuario.save()
                    return render(request, 'AppCommerce/bienvenida.html', {"usuario"})
                else:
                    return render(request, "AppCommerce/register.html", {"falla_contrasenia":True})
        return render(request, "AppCommerce/register.html")


def login(request):
        if request.method == 'POST':
            try:
                usuario = Usuario.objects.get(email=request.POST['email'])
                if usuario.contrasenia == request.POST['contrasenia']:
                    return render(request, 'AppCommerce/bienvenida.html', {"usuario":usuario})     
                return render(request, 'AppCommerce/login.html', {"contrasenia_invalida":True})
            except:
                 return render(request, 'AppCommerce/login.html', {"usuario_inexistente":True})
        return render(request, "AppCommerce/login.html")