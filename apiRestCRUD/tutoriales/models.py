from django.db import models

# Create your models here.
class Tutoriales(models.Model):
    titulo = models.CharField(max_length=20, blank=False, default='Sin titulo')
    detalle = models.CharField(max_length=20, blank=False, default='Sin detalle')
    publicado = models.BooleanField(default=False)