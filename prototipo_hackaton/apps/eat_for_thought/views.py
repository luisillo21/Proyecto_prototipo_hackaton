from django.shortcuts import render
import hashlib
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import *
from django.urls import reverse_lazy
from django.urls import reverse
from .models import *
from apps.usuario.forms import *
from .forms import *


def buscar_formulario(request):
    context = {}
    context['paises'] = Pais.objects.all().select_related('id_region')
    context['regiones'] = Region.objects.all().select_related('id_provinvia')
    context['cosecha'] = Cosecha.objects.all().select_related('')
    
    return render(request,'eat_for_thought/form_search.html',context)


class List_cosecha(ListView):
    model = Cosecha
    template_name = 'Mantenimiento/listar_cosecha.html'

class CreateGeneral (CreateView):
    model = Cosecha
    template_name = 'Mantenimiento/agregar_cosecha.html'
    form_class = Cosecha_1
    success_url = reverse_lazy('vase')
#no terminado
def eliminar_cosecha(request,id_cosecha):
    cosecha = Cosecha.objects.get( id_cosecha= id_cosecha)
    if request.method == 'POST':
        cosecha.delete()
        return redirect ('listar_cosecha')
    return render(request,'Mantenimiento/eliminar_materia.html',{'cosecha':cosecha})
#no terminado

class Updatecosecha (UpdateView):
    model = Cosecha
    template_name = 'Mantenimiento/editar_cosecha.html'
    form_class = Cosecha_1
    success_url = reverse_lazy('listar_cosecha')
    context_object_name = 'F'
