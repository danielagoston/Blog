from django.shortcuts import render
from .models import Post, Categoria

def home(request):
    posts = Post.objects.filter(estado = True)
    return render (request, 'index.html', {'posts':posts})

def detallePost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    return render(request,'post.html', {'detalle_post':post})
def about(request):
    posts = Post.objects.filter(
        estado = True, 
        categoria = Categoria.objects.get(nombre = '¿Quiénes Somos?'))
    return render (request, 'about.html', {'posts':posts})

def anecdotes(request):
    posts = Post.objects.filter(
        estado = True, 
        categoria = Categoria.objects.get(nombre = 'Anécdotas'))
    return render (request, 'anecdotes.html', {'posts':posts})

def purpose(request):
    posts = Post.objects.filter(
        estado = True, 
        categoria = Categoria.objects.get(nombre = 'Propósito'))
    return render (request, 'purpose.html', {'posts':posts})