from django.db import models
from apps.eat_for_thought.models import *
from django.db.models import AutoField


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length= 200,blank=False, null=False)
    id_pais = models.ForeignKey(Pais)
    id_region = models.ForeignKey(Region)
    edad = models.CharField(max_length= 200,blank=False, null=False,)
    foto = models.CharField(max_length= 2,blank=False, null=False,)
    correo = models.CharField(max_length= 200,blank=False, null=False,)
    id_provincia = models.ForeignKey(Provincia)
    sudonimo = models.CharField(max_length= 200,blank=False, null=False,)


    def __str__(self):
        return self.nombre