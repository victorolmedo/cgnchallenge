from rest_framework import serializers
from libros.models import Autor, Libro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad', 'fecha_nacimiento']


class LibroSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'fecha_publicacion', 'isbn', 'autores']