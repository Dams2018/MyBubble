from django.contrib import admin
# importando base de datos
from app.web.models import Usuario, Tipo_Usuario, Avatar, Comentario, Curso, Asignatura, Pregunta, Respuesta, Puente
# Register your models here.


admin.site.register(Usuario)
admin.site.register(Tipo_Usuario)
admin.site.register(Avatar)
admin.site.register(Comentario)
admin.site.register(Curso)
admin.site.register(Asignatura)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Puente)

