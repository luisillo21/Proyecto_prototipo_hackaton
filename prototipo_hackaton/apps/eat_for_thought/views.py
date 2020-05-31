from django.shortcuts import render
import hashlib
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import *
from django.urls import reverse_lazy
from django.urls import reverse
from .models import *
from apps.usuario.forms import *

def buscar_formulario(request):
    context = {}
    context['paises'] = Pais.objects.all().select_related('id_region')
    context['regiones'] = Region.objects.all().select_related('id_provinvia')
    context['cosecha'] = Cosecha.objects.all().select_related('')
    
    return render(request,'eat_for_thought/form_search.html',context)
