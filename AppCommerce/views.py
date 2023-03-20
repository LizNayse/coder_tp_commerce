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
                    billetera = Billetera (usuario=usuario, efectivo=0)
                    billetera.save()
                    return render(request, 'AppCommerce/usuario.html', {"usuario":usuario})
                else:
                    return render(request, "AppCommerce/register.html", {"falla_contrasenia":True})
        return render(request, "AppCommerce/register.html")


def login(request):
        if 'usuario_id' in request.session:
             u_id = request.session['usuario_id']
             usuario = Usuario.objects.get(pk=u_id)
             return render(request, 'AppCommerce/usuario.html', {"usuario":usuario})
        if request.method == 'POST':
            try:
                usuario = Usuario.objects.get(email=request.POST['email'])
                if usuario.contrasenia == request.POST['contrasenia']:
                    request.session['usuario_id'] = usuario.id
                    return render(request, 'AppCommerce/usuario.html', {"usuario":usuario})     
                return render(request, 'AppCommerce/login.html', {"contrasenia_invalida":True})
            except:
                 return render(request, 'AppCommerce/login.html', {"usuario_inexistente":True})
        return render(request, "AppCommerce/login.html")

def logout(request):
     del request.session['usuario_id']
     return render(request, 'AppCommerce/login.html')

def billetera(request, usuarioid):
    usuario = Usuario.objects.get(pk=usuarioid)
    if request.method == 'POST':
        usuario.billetera.efectivo +=  int(request.POST['efectivo'])
        usuario.billetera.save()
    return render(request, "AppCommerce/billetera.html", {"usuario":usuario})