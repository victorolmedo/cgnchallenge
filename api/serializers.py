from rest_framework import serializers
from libros.models import Autor, Libro


class AutorSerializer(serializers.ModelSerializer):
    #Campo calculado
    total_libros = serializers.IntegerField(read_only=True)

    class Meta:
        model = Autor
        fields = '__all__'
        extra_kwargs = {
            'fecha_nacimiento': {'required': False},
        }


class LibroSerializer(serializers.ModelSerializer):
    # Detalle de autores
    autores = AutorSerializer(many=True, read_only=True)

    # para las escritureas del POST PUT
    autores_ids = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(),
        source='autores',
        many=True,
        write_only=True,
        required=False,
        allow_empty=True
    )

    class Meta:
        model = Libro
        fields = '__all__'
