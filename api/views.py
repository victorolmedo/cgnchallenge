from django.db.models import Count, Avg, Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from libros.models import Autor, Libro
from api.serializers import AutorSerializer, LibroSerializer


class StandardPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.annotate(total_libros=Count('libro'))  # Consulta base
    serializer_class = AutorSerializer
    pagination_class = StandardPagination

    # Consulta con annotate
    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        # Primero anotamos la cantidad de libros por autor
        autores_annotated = Autor.objects.annotate(total_libros=Count('libro'))
        # Luego calculamos el promedio
        promedio = autores_annotated.aggregate(promedio_libros=Avg('total_libros'))

        return Response(promedio)


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        anio = self.request.query_params.get('anio')
        nacionalidad = self.request.query_params.get('nacionalidad')

        if anio and nacionalidad:
            # Usar Q para filtros complejas
            queryset = queryset.filter(
                Q(fecha_publicacion__year__gte=anio) &
                Q(autores__nacionalidad=nacionalidad)
            ).distinct()

        return queryset
