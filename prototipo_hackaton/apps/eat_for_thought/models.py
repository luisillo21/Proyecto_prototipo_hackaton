from django.db import models
from  apps.usuario.models import *

class Provincia(models.Model):
    id_provincia= models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length= 20,blank=False, null=False)
    planta = models.CharField(max_length= 20,blank=False, null=False)


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region= models.CharField('ingrese la region',max_length=50, blank=False, null=False)
    temperatura = models.CharField(max_length= 20,blank=False, null=False)
    id_provinvia = models.ForeignKey(Provincia)
    plantas =  models.CharField(max_length= 20,blank=False, null=False)



class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField('Nombre de pais',max_length=50, blank=False, null=False)
    id_region = models.ForeignKey(Region)
    def __str__(self):
        return self.nombre_pais


