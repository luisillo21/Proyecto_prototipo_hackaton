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
from .utils import link_callback
from django.template.loader import get_template
from xhtml2pdf import pisa
import requests

def result_search(request):
    context = {}
    if request.method == 'POST':
        context['data'] = Provincia.objects.get(id_provincia=request.POST.get('provincia'))
        context['detalles_rec'] = Cosecha.objects.filter()
        return render(request,'eat_for_thought/form_results.html',context)
    return render(request,'eat_for_thought/form_results.html',context)

def generate_request(params={}):
    url = "https://power.larc.nasa.gov/downloads/POWER_Regional_Daily_20200105_20200307_61d639b3.json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    return response.get('features')[0].get('geometri')


def buscar_formulario(request):
    context = {}
    context['provincias'] = Provincia.objects.all()
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

class MostrarDetalle(UpdateView):
    model = Cosecha
    form_class = Cosecha_1
    template_name = 'eat_for_thought/mostar_detalle.html'
    context_object_name = 'F'

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


#----------------------------Report section------------------
def informacion_cosecha(request,id):
    template_path = 'reportes/info_cosecha.html'
    context = {}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
