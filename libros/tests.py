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

    def test_contar_libros_por_autor(self):
        # Crear autores
        autor1 = Autor.objects.create(nombre="Autor 1")
        autor2 = Autor.objects.create(nombre="Autor 2")

        # Crear libros y asignarlos explícitamente
        libro1 = Libro.objects.create(titulo="Libro 1", fecha_publicacion="2023-01-01", isbn="111")
        libro2 = Libro.objects.create(titulo="Libro 2", fecha_publicacion="2023-01-02", isbn="222")
        libro3 = Libro.objects.create(titulo="Libro 3", fecha_publicacion="2023-01-03", isbn="333")

        # Asignar 2 libros al primer autor y 1 al segundo
        autor1.libro_set.add(libro1, libro2)
        autor2.libro_set.add(libro3)

        # Obtener la lista de autores desde la API
        response = self.client.get(reverse('autor-list'))

        # Buscar el autor1 en la respuesta (puede no ser el primero en la lista)
        autor_data = next((a for a in response.data if a['id'] == autor1.id), None)

        self.assertIsNotNone(autor_data)
        self.assertEqual(autor_data['total_libros'], 2)  # ¡Ahora sí 2 libros!


# libros/tests.py
def test_promedio_libros_por_autor(self):
    # Crear autores y libros de prueba
    autor1 = Autor.objects.create(nombre="Autor 1")
    autor2 = Autor.objects.create(nombre="Autor 2")
    Libro.objects.create(titulo="Libro 1").autores.add(autor1)
    Libro.objects.create(titulo="Libro 2").autores.add(autor1)
    Libro.objects.create(titulo="Libro 3").autores.add(autor2)

    # Hacer la petición
    response = self.client.get(reverse('autor-estadisticas'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['promedio_libros'], 1.5)  # (2 libros + 1 libro) / 2 autores = 1.5