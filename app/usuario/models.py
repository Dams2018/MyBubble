from django.db import models

# Create your models here.
class Curso(models.Model):
    idCurso=models.AutoField(primary_key=True)
    nombreCurso=models.CharField(max_length=30)
    activo=models.BooleanField(default=True)
    
class Tipo_Usuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=10) 
    
class Avatar(models.Model):
    idAvatar=models.AutoField(primary_key=True)
    imagen=models.CharField(max_length=50)
    puntosAvatar=models.IntegerField(default=0)

class Usuario(models.Model):
    idUsuario=models.AutoField(primary_key=True)
    run=models.CharField(max_length=12, default= 1)  
    nombre = models.CharField(max_length=25)
    apaterno = models.CharField(max_length=25)
    apmaterno = models.CharField(max_length=25)
    correo = models.EmailField(max_length=50)
    activo = models.BooleanField(default = True)
    puntos = models.IntegerField(default = 0)
    idTipoUsuario = models.ForeignKey(Tipo_Usuario, null = True, blank = True, on_delete = models.DO_NOTHING)
    idAvatar = models.ForeignKey(Avatar, null = True, blank = True, on_delete = models.DO_NOTHING)
    idCurso = models.ForeignKey(Curso, null = True, blank = True, on_delete = models.DO_NOTHING)

class Comentario(models.Model):
    idComentario = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length= 20)
    descripcion = models.CharField(max_length = 250)
    idUsuario = models.ForeignKey(Usuario, null = True, blank = True, on_delete = models.DO_NOTHING)


