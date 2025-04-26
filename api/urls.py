from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutorViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet, basename='libros-api')
router.register(r'autores', AutorViewSet, basename='autores-api')

urlpatterns = [
    path('', include(router.urls)),
]