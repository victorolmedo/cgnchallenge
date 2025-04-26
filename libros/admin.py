from django.contrib import admin
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
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento')
    search_fields = ('nombre', 'nacionalidad')


@admin.register(Libro)
class LibroAdmin(ImportExportModelAdmin):
    # Habilita import/export
    resource_class = LibroResource
    list_display = ('titulo', 'fecha_publicacion', 'isbn')
    filter_horizontal = ('autores',)
    search_fields = ('titulo', 'isbn')
