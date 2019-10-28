from django.db import models

# Create your models here.
# Create your models here.


class feed(models.Model):
	id=models.IntegerField(primary_key=True)
	author=models.CharField(max_length=50)
	title=models.CharField(max_length=100)
	body=models.TextField()

    
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
    run=models.CharField(max_length=12)  
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

class Asignatura(models.Model):
    idAsignatura=models.CharField(max_length=20, primary_key=True)
    nombreAsigantura=models.CharField(max_length=15)
    activo=models.BooleanField(default=True)
    idcurso=models.ForeignKey(Curso, null=True, blank=True, on_delete= models.DO_NOTHING)

class Pregunta(models.Model):
    id_Pregunta=models.AutoField(primary_key=True)
    pregunta=models.CharField(max_length=100)
    activopregunta=models.BooleanField(default=True)

class Respuesta(models.Model):
    id_Respuesta=models.AutoField(primary_key=True)
    respuestas=models.CharField(max_length=100)
    correcta=models.BooleanField(default=False)
    id_Pregunta=models.ForeignKey(Pregunta, null=True, blank=True, on_delete= models.DO_NOTHING)
    idUsuario = models.ForeignKey(Usuario, null = True, blank = True, on_delete = models.DO_NOTHING)


class Puente(models.Model):
    id_Pregunta=models.ForeignKey(Pregunta, null=True, blank=True, on_delete= models.DO_NOTHING)
    idUsuario = models.ForeignKey(Usuario, null = True, blank = True, on_delete = models.DO_NOTHING)
    id_Respuesta = models.ForeignKey(Respuesta, null = True, blank = True, on_delete = models.DO_NOTHING)