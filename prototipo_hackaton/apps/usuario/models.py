from django.db import models
from apps.eat_for_thought.models import *
# Create your models here.


class Usuario(models.Model):
    nombres = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    correo = models.EmailField(max_length=100, blank=False, null=False)
    clave = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'Usuario',
        verbose_name_plural = 'Usuarios',
        db_table = 'usuario'

    def __str__(self):
        return self.nombres
