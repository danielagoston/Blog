from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    # Obtener el valor del parámetro de consulta llamado "buscar"
    queryset = request.GET.get("buscar")
    
    # Filtrar todas las publicaciones que tienen estado activo
    posts = Post.objects.filter(estado=True)
    
    # Si hay un valor en el parámetro de consulta "buscar"
    if queryset:
        # Filtrar las publicaciones que contienen el valor de búsqueda en el título o la descripción
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |  # Filtrar por título que contiene el valor de búsqueda
            Q(descripcion__icontains=queryset)  # Filtrar por descripción que contiene el valor de búsqueda
        ).distinct()  # Eliminar duplicados en el resultado

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    # Renderizar la plantilla 'index.html' y pasar el conjunto de publicaciones como contexto
    return render(request, 'index.html', {'posts': posts})

def detallePost(request, slug):
    # Obtener la publicación correspondiente al slug dado, o devolver un error 404 si no se encuentra
    post = get_object_or_404(Post, slug=slug)
    # Renderizar la plantilla 'post.html' y pasar los detalles de la publicación como contexto
    return render(request, 'post.html', {'detalle_post': post})

def about(request):
    # Obtener el valor del parámetro de consulta llamado "buscar"
    queryset = request.GET.get("buscar")
    # Filtrar las publicaciones que tienen estado activo y pertenecen a la categoría "¿Quiénes Somos?"
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='¿Quiénes Somos?')  # Filtrar por la categoría específica
    )
    if queryset:
        # Filtrar las publicaciones que contienen el valor de búsqueda en el título o la descripción
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |  # Filtrar por título que contiene el valor de búsqueda
            Q(descripcion__icontains=queryset)  # Filtrar por descripción que contiene el valor de búsqueda
        ).distinct()  # Eliminar duplicados en el resultado
    
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # Renderizar la plantilla 'about.html' y pasar el queryset de publicaciones como contexto
    return render(request, 'about.html', {'posts': posts})

def anecdotes(request):
    # Obtener el valor del parámetro de consulta llamado "buscar"
    queryset = request.GET.get("buscar")
    # Filtrar las publicaciones que tienen estado activo y pertenecen a la categoría "Anécdotas"
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Anécdotas')  # Filtrar por la categoría específica
    )
    if queryset:
        # Filtrar las publicaciones que contienen el valor de búsqueda en el título o la descripción
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |  # Filtrar por título que contiene el valor de búsqueda
            Q(descripcion__icontains=queryset)  # Filtrar por descripción que contiene el valor de búsqueda
        ).distinct()  # Eliminar duplicados en el resultado
    # Renderizar la plantilla 'anecdotes.html' y pasar el queryset de publicaciones como contexto
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'anecdotes.html', {'posts': posts})

def purpose(request):
    # Obtener el valor del parámetro de consulta llamado "buscar"
    queryset = request.GET.get("buscar")
    # Filtrar las publicaciones que tienen estado activo y pertenecen a la categoría "Propósito"
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Propósito')  # Filtrar por la categoría específica
    )
    if queryset:
        # Filtrar las publicaciones que contienen el valor de búsqueda en el título o la descripción
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |  # Filtrar por título que contiene el valor de búsqueda
            Q(descripcion__icontains=queryset)  # Filtrar por descripción que contiene el valor de búsqueda
        ).distinct()  # Eliminar duplicados en el resultado
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # Renderizar la plantilla 'purpose.html' y pasar el queryset de publicaciones como contexto
    return render(request, 'purpose.html', {'posts': posts})