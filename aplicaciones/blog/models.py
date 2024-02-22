from django.db import models

# Definición del modelo Categoria
class Categoria(models.Model):
    # Campo para el identificador único de la categoría
    id = models.AutoField(primary_key=True)
    # Campo para el nombre de la categoría
    nombre = models.CharField('Nombre de la Categoría', max_length=100, null=False, blank=False)
    # Campo para indicar si la categoría está activada o no
    estado = models.BooleanField('Categoría Activada/Categoría no Activada', default=True)
    # Campo para la fecha de creación de la categoría
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    # Método para representar la categoría como una cadena
    def __str__(self):
        return self.nombre
    
# Definición del modelo Autor
class Autor(models.Model):
    # Campo para el identificador único del autor
    id = models.AutoField(primary_key=True)
    # Campos para el nombre y apellidos del autor
    nombres = models.CharField('Nombres del Autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellidos del Autor', max_length=255, null=False, blank=False)
    # Campos para las redes sociales y el sitio web del autor
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    # Campo para el correo electrónico del autor
    correo = models.EmailField('Correo Electrónico', null=False, blank=False)
    # Campo para indicar si el autor está activo o no
    estado = models.BooleanField('Autor Activo/ No Activo', default=True)
    # Campo para la fecha de creación del autor
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    # Método para representar al autor como una cadena
    def __str__(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)