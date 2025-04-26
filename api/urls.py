from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutorViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet, basename='libro')
router.register(r'autores', AutorViewSet, basename='autor')

urlpatterns = [
    path('', include(router.urls)),
]