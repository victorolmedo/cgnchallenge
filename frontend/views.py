# frontend/views.py
from django.shortcuts import render
from libros.models import Libro


def home(request):
    return render(request, 'home.html')
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'frontend/lista_libros.html', {'libros': libros})