"""
Configuración de WSGI para el proyecto mysite.

Este archivo expone la aplicación WSGI como una variable a nivel de módulo llamada application.
"""

# Importamos la funcion "os" para interactuar con el sistema operativo
import os

# Importamos la función "get_wsgi_application" para configurar la aplicación WSGI
from django.core.wsgi import get_wsgi_application

# Configuramos el archivo de configuración del proyecto (asegura que se use el archivo "settings.py" correctamente).
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Creamos la instancia WSGI (usada para manejar las solicitudes).
application = get_wsgi_application()

