from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Categoria, Autor, Post

# Definimos un recurso de importación/exportación para la clase Categoria
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria  # Especificamos el modelo que este recurso va a manejar

# Definimos un recurso de importación/exportación para la clase Autor
class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor  # Especificamos el modelo que este recurso va a manejar

# Definimos una clase de administrador para la clase Categoria, que hereda de ImportExportModelAdmin y admin.ModelAdmin
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']  # Especificamos los campos de búsqueda para el panel de administración
    list_display = ('nombre', 'estado', 'fecha_creacion',)  # Especificamos los campos a mostrar en la lista
    resource_class = CategoriaResource  # Especificamos el recurso de importación/exportación para esta clase

# Definimos una clase de administrador para la clase Autor, que hereda de ImportExportModelAdmin y admin.ModelAdmin
class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'correo']  # Especificamos los campos de búsqueda para el panel de administración
    list_display = ('nombres', 'apellidos', 'correo', 'estado', 'fecha_creacion',)  # Especificamos los campos a mostrar en la lista
    resource_class = AutorResource  # Especificamos el recurso de importación/exportación para esta clase

# Registramos las clases de administrador en el panel de administración de Django
admin.site.register(Categoria, CategoriaAdmin)  # Registramos la clase Categoria con su respectivo administrador
admin.site.register(Autor, AutorAdmin)  # Registramos la clase Autor con su respectivo administrador
admin.site.register(Post)  # Registramos la clase Post en el panel de administración