from django.db.models import Count
from rest_framework import viewsets
from libros.models import Autor, Libro
from api.serializers import AutorSerializer, LibroSerializer


class AutorViewSet(viewsets.ModelViewSet):
    # Consulta con annotate
    queryset = Autor.objects.annotate(total_libros=Count('libro'))
#   queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer