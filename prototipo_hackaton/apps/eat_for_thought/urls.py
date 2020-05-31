from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.eat_for_thought.views import *
from django.views.generic import TemplateView
from django.urls import path, include


from apps.eat_for_thought.views import *
from apps.usuario import views
from django.views.generic import TemplateView

urlpatterns = [
    path('form_search/',buscar_formulario, name='form_search'),
    path('crear_cosecha/', CreateGeneral.as_view(), name='crear_cosecha'),
    path('listar_cosecha/', List_cosecha.as_view(), name='listar_cosecha'),
    path('update_cosecha/<int:pk>', Updatecosecha.as_view(), name='update_cosecha'),
    path('eliminar_cosecha/<int:pk>', Eliminar_cosecha.as_view(), name='eliminar_cosecha')

]