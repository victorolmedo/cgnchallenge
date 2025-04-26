from django.contrib import admin
from django.db.models import Count
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from libros.models import Autor, Libro


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro


@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    fields = ['nombre', 'nacionalidad', 'fecha_nacimiento']
    # Habilita import/export
    resource_class = AutorResource
    list_display = ('nombre', 'nacionalidad', 'total_libros')
    search_fields = ('nombre', 'nacionalidad')
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(total_libros=Count('libro'))

    def total_libros(self, obj):
        return obj.total_libros
    total_libros.admin_order_field = 'total_libros'

@admin.register(Libro)
class LibroAdmin(ImportExportModelAdmin):
    # Habilita import/export
    resource_class = LibroResource
    list_display = ('titulo', 'fecha_publicacion', 'isbn')
    filter_horizontal = ('autores',)
    search_fields = ('titulo', 'isbn')
