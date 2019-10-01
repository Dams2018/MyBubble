from django.db import models

# Create your models here.
class Tipo_Usuario(models.Model):
    idTipoUsuario = models.CharField(max_length=10, primary_key = True)
    descripcion = models.CharField(max_length=10) 
    
class Usuario(models.Model):
    idUsuario=models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=25)
    apaterno = models.CharField(max_length=25)
    apmaterno = models.CharField(max_length=25)
    correo = models.EmailField(max_length=50)
    activo = models.BooleanField(default = True)
    puntos = models.IntegerField(default = 0)
    idTipoUsuario = models.ForeignKey(Tipo_Usuario, null=True, blank = True, on_delete = models.DO_NOTHING)

