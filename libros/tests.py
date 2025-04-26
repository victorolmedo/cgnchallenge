from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from libros.models import Autor, Libro

class ModelTests(TestCase):
    def setUp(self):
        # Crear datos de prueba para modelos
        self.autor = Autor.objects.create(
            nombre="Gabriel García Márquez",
            nacionalidad="Colombiana",
            fecha_nacimiento="1927-03-06"
        )
        self.libro = Libro.objects.create(
            titulo="Cien años de soledad",
            isbn="9780307474728"
        )
        self.libro.autores.add(self.autor)

    def test_autor_creado_correctamente(self):
        """Verificar que el autor se creó con los datos correctos"""
        self.assertEqual(self.autor.nombre, "Gabriel García Márquez")
        self.assertEqual(self.autor.nacionalidad, "Colombiana")

    def test_libro_tiene_autores(self):
        """Verificar la relación ManyToMany entre Libro y Autor"""
        self.assertEqual(self.libro.autores.count(), 1)
        self.assertIn(self.autor, self.libro.autores.all())

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.autor = Autor.objects.create(
            nombre="Julio Cortázar",
            nacionalidad="Argentina",
            fecha_nacimiento="1914-08-26"
        )
        self.libro = Libro.objects.create(
            titulo="Rayuela",
            isbn="9788437603587"
        )
        self.libro.autores.add(self.autor)
        self.url_autores = reverse('autor-list')
        self.url_libros = reverse('libro-list')

    def test_listar_autores(self):
        """GET /api/autores/ debe retornar 200 OK"""
        response = self.client.get(self.url_autores)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.autor.nombre)

    def test_crear_libro(self):
        """POST /api/libros/ debe crear un libro con autores"""
        payload = {
            "titulo": "La casa de los espíritus",
            "fecha_publicacion": "1982-01-01",
            "isbn": "9780525433472",
            "autores_ids": [self.autor.id]
        }
        response = self.client.post(self.url_libros, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Libro.objects.count(), 2)