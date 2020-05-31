from django.shortcuts import render,render_to_response
import hashlib
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import *
from django.urls import reverse_lazy
from django.urls import reverse
from .models import *
from apps.usuario.forms import *
from .forms import *


def result_search(request):
    context = {}
    return render(request,'eat_for_thought/form_results.html',context)


def buscar_formulario(request):
    context = {}
    context['regiones'] = Region.objects.all()
    context['cosechas'] = Cosecha.objects.all().values('id_cosecha','nombre_cosecha')
    if request.method  == 'POST':
        #region = request.POST.get('region')
        cosecha = request.POST.get('cosecha')
        if cosecha == 'Todos':
            context['cosechas_search'] = Cosecha.objects.filter()
            return render(request, 'eat_for_thought/form_search.html', context)
        else:
            if Cosecha.objects.filter().exists():
                context['cosecha'] = Cosecha.objects.filter().get(id_cosecha=cosecha)
                return render(request, 'eat_for_thought/form_search.html', context)

    return render(request,'eat_for_thought/form_search.html',context)


class List_cosecha(ListView):
    model = Cosecha
    template_name = 'Mantenimiento/listar_cosecha.html'

class CreateGeneral (CreateView):
    model = Cosecha
    template_name = 'Mantenimiento/agregar_cosecha.html'
    form_class = Cosecha_1
    success_url = reverse_lazy('listar_cosecha')

class Eliminar_cosecha (DeleteView):
    model = Cosecha
    template_name = 'Mantenimiento/eliminar_cosecha.html'
    success_url = reverse_lazy('listar_cosecha')
    context_object_name = 'F'


class Updatecosecha (UpdateView):
    model = Cosecha
    template_name = 'Mantenimiento/editar_cosecha.html'
    form_class = Cosecha_1
    success_url = reverse_lazy('listar_cosecha')
    context_object_name = 'F'

class List_dealleCosecha(ListView):
    model = DetalleCosecha
    template_name = 'Mantenimiento/listar_detallecosechas.html'

class Createdetalles (CreateView):
    model = Cosecha
    template_name = 'Mantenimiento/agregar_cosecha.html'
    form_class = Cosecha_1
    success_url = reverse_lazy('listar_cosecha')

class Eliminar_cosecha (DeleteView):
    model = Cosecha
    template_name = 'Mantenimiento/eliminar_cosecha.html'
    success_url = reverse_lazy('listar_cosecha')
    context_object_name = 'F'


class Updatecosecha (UpdateView):
    model = Cosecha
    template_name = 'Mantenimiento/editar_cosecha.html'
    form_class = Cosecha_1
    success_url = reverse_lazy('listar_cosecha')
    context_object_name = 'F'
