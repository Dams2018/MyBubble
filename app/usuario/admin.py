from django.contrib import admin
# importando base de datos
from app.usuario.models import Usuario, Tipo_Usuario, Avatar, Comentario, Curso
# Register your models here.


admin.site.register(Usuario)
admin.site.register(Tipo_Usuario)
admin.site.register(Avatar)
admin.site.register(Comentario)
admin.site.register(Curso)

