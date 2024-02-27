from django.urls import path
from .views import home, about, anecdotes, purpose,detallePost

urlpatterns = [
    path('',home, name = 'index'),
    path('<slug:slug>/', detallePost, name = 'detalle_post'),
    path('about/', about, name = 'about'),
    path('anecdotes/', anecdotes, name = 'anecdotes'),
    path('purpose/', purpose, name = 'purpose'),

]