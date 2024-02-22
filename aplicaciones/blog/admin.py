from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'correo']
    list_display = ('nombres','apellidos','correo', 'estado', 'fecha_creacion',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
