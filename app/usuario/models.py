from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario=models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=25)
    appaterno = models.CharField(max_length=25)
    apmaterno = models.CharField(max_length=25)
    correo = models.EmailField(max_length=50)
    #activo = models.
    #puntos = models