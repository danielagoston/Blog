from django.shortcuts import render

def home(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def anecdotes(request):
    return render (request, 'anecdotes.html')

def purpose(request):
    return render (request, 'purpose.html')