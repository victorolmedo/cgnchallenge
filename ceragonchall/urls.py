from django.contrib import admin
from django.urls import path, include
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'))),
    path('libros/', include('libros.urls', namespace='libros')),
    path('', include('frontend.urls')),
    path('', views.home, name='home'),
]