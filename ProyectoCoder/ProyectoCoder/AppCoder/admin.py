from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Curso)

admin.site.register(Jugador)


admin.site.register(Equipo)

admin.site.register(Estadio)

admin.site.register(Empleado)


