from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField(null=True, blank=True)
    autores = models.ManyToManyField(Autor)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo