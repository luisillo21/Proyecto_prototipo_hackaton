from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.usuario.views import *
from apps.usuario import views
from django.views.generic import TemplateView

urlpatterns = [
    path('base', views.base, name='vase'),
    path('', views.index, name='index'),
    path('crear_usuario/', Usuarios.as_view(), name='crear_usuario'),
    path('formulario/', Formulario.as_view(), name='formulario'),
    path('informacion/', Informacion.as_view(), name='informacion'),
    path('mapa/', Mapa.as_view(), name='mapa'),
    path('cerrarsession/', cerrarsesion, name='cerrarsesion'),


]