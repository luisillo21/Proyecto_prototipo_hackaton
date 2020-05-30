from django.shortcuts import render
import hashlib
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import *
from django.urls import reverse_lazy
from django.urls import reverse
from .models import *
from .forms import *

def index(request):
    return render(request, "login.html")

class Usuarios(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'crear_cuenta.html'
    success_url = ('login')

class Formulario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'formulario.html'
    success_url = ('formulario')

class Informacion(ListView):
    model = Usuario
    template_name = 'informacion.html'

class Mapa(ListView):
    model = Usuario
    template_name = 'mapa.html'
