from rest_framework import serializers
from libros.models import Autor, Libro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    # Detalle de autores
    autores = AutorSerializer(many=True, read_only=True)

    # para las escritureas del POST PUT
    autores_ids = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(),
        source='autores',
        many=True,
        write_only=True,
        required = False,
        allow_empty = True
    )

    class Meta:
        model = Libro
        fields = '__all__'
