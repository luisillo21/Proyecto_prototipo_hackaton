from django.db import models
from apps.usuario.models import *

class Provincia(models.Model):
    id_provincia= models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=20, blank=False, null=False)
    planta = models.CharField(max_length=20, blank=False, null=False)


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region= models.CharField('ingrese la region',max_length=50, blank=False, null=False)
    temperatura = models.CharField(max_length=20, blank=False, null=False)
    id_provinvia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    plantas =  models.CharField(max_length=20, blank=False, null=False)



class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField('Nombre de pais', max_length=50, blank=False, null=False)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE,related_name='region_pais')
    def __str__(self):
        return self.nombre_pais


class Cosecha(models.Model): 
    COSECHA_CHOICES = [('frutas', 'Fruta'), ('Vegetales', 'Vegetales')]
    tipo_cosecha = models.CharField(max_length=50 , choices=COSECHA_CHOICES)
    id_cosecha = models.AutoField(primary_key=True)
    nombre_cosecha = models.CharField(max_length=50)
    descripcion = models.TextField()
    vitamina = models.CharField(max_length=100)
    temperatura = models.CharField(max_length=100)
    tiempo_de_riego = models.CharField(max_length=150)
    humedad_de_tierra = models.CharField(max_length=150)
    class Meta:
        verbose_name = 'Cosecha',
        verbose_name_plural = 'Cosechas',
        db_table = 'Cosecha'
    def __str__(self):
        return self.nombre_cosecha

    def detalle_cosecha(self):
        detalle = DetalleCosecha.objects.filter(cosecha=self.id_cosecha)
        return detalle


class DetalleCosecha(models.Model):
    cosecha = models.ForeignKey(Cosecha, on_delete=models.CASCADE,related_name='detalle_cosecha')
    curacion_Cosecha = models.CharField(max_length=150)
    casos_de_cosecha = models.TextField()
    foto = models.ImageField(upload_to='imagenes_cosecha/')
    vide_instuctivo = models.URLField()

    class Meta:
        verbose_name = 'DetalleCosecha',
        verbose_name_plural = 'DetalleCosechas',
        db_table = 'DetalleCosecha'


    def __str__(self):
        return self.cosecha.nombre_cosecha




