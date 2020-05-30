from django.shortcuts import render
import hashlib
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import *
from django.urls import reverse_lazy
from django.urls import reverse
from .models import *
from .forms import *


def base(request):
    return render(request, "base.html")


def index(request):
    #return render(request, "login.html")
    contexto = {}
    try:
        if request.method == 'POST':
            var_usuario = request.POST.get('usu')
            var_contra = request.POST.get('pass')
            #h = hashlib.new("sha1")
            #var_contra = str.encode(var_contra)
            #h.update(var_contra)
            #print(h.hexdigest())
            if Usuario.objects.filter(correo=var_usuario, clave=var_contra).exists():
                usu = Usuario.objects.get(correo=var_usuario, clave=var_contra)
                request.session['usuario'] = usu.id
                return redirect("vase")
            else:
                contexto['error'] = "Usuario o contraseña incorrectos"
                return render(request, 'login.html', contexto)
    except Exception as e:
        print(e)
        contexto['error'] = "Usuario o contraseña incorrectos"
        return render(request, 'login.html', contexto)
    return render(request, 'login.html', contexto)









class Usuarios(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'crear_cuenta.html'
    success_url = reverse_lazy('index')


class Formulario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('formulario')

class Informacion(ListView):
    model = Usuario
    template_name = 'informacion.html'

class Mapa(ListView):
    model = Usuario
    template_name = 'mapa.html'
