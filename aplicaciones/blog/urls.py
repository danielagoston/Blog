from django.urls import path
from .views import home, about, anecdotes, purpose

urlpatterns = [
    path('',home, name = 'index'),
    path('about/',about, name = 'about'),
    path('anecdotes/',anecdotes, name = 'anecdotes'),
    path('purpose/',purpose, name = 'purpose'),

]