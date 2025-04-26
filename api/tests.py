from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from libros.models import Autor, Libro


class AutorAPITests(TestCase):
    """Test la API de Autores"""

    def setUp(self):
        self.client = APIClient()
        self.autor = Autor.objects.create(
            nombre="Julio Cortázar",
            nacionalidad="Argentina"
        )
        self.url = reverse('autor-list')

    def test_listar_autores(self):
        """Test: Listar autores (GET)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.autor.nombre)

    def test_crear_autor(self):
        """Test: Crear autor (POST)"""
        payload = {
            "nombre": "Isabel Allende",
            "nacionalidad": "Chilena",
            "fecha_nacimiento": "1942-08-02"
        }
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 2)