from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.eat_for_thought.views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('form_search/',buscar_formulario, name='form_search'),
]