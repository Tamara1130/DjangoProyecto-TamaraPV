"""
Configuración ASGI para el proyecto mysite.

Este archivo pone a ASGI como una variable a nivel de módulo llamada ``application``.
"""

import os  # Importamos este modulo para interactuar con las variables de entorno

# Importamos la función que nos permite obtener ASGI de Django
from django.core.asgi import get_asgi_application

# Establecemos el modulo de configuración de Django que se usara en esta seccion
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Creamos la aplicación ASGI (interfaz de servidor para aplicaciones web)
application = get_asgi_application()
