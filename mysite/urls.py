"""
Configuración de URLs para el proyecto mysite.

La lista `urlpatterns` enruta las URLs a las vistas correspondientes.
"""

# Importamos las funciones necesarias
from django.contrib import admin  # Interfaz administrativa de Django
from django.urls import path, include  # path: para definir rutas
from app.views import random_graphs  # Importamos la vista de "random_graphs"

# Patrones de URLs para el proyecto
urlpatterns = [
    # Ruta para la interfaz de administración
    path('admin/', admin.site.urls),
    
    # Ruta del proyecto asignada a la vista "random_graphs" de la app
    path('', random_graphs, name='random_graphs'),
    
    # Incluimos las URLs definidas en la aplicación "app" (esto busca un archivo "urls.py" dentro de la carpeta "app").
    path('app/', include('app.urls')),
]

