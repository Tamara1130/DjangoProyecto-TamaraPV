"""
Configuración de Django para el proyecto mysite.

Generado por 'django-admin startproject' usando Django 5.1.3.
"""

# Importamos Path para trabajar con rutas de archivos
from pathlib import Path

# Establecemos la ruta base (carpeta principal que contiene este archivo).
BASE_DIR = Path(__file__).resolve().parent.parent

# ADVERTENCIA DE SEGURIDAD: Mantener la clave secreta en producción oculta
SECRET_KEY = 'django-insecure-*%#zt+j^=g^l6#wb_-n3k)#qlm6ui27le(&0)hxb1x9lok4_&7'

# ADVERTENCIA DE SEGURIDAD: No dejar el modo DEBUG activado en producción
DEBUG = True  # En producción, siempre deberías poner DEBUG a False

# Especificamos qué direcciones IP pueden acceder a la aplicación
ALLOWED_HOSTS = []


# Definicion de las aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    'django.contrib.admin',  # Interfaz de administración de Django
    'django.contrib.auth',  # Gestión de autenticación de usuarios
    'django.contrib.contenttypes',  # Gestor de modelos de contenido
    'django.contrib.sessions',  # Soporte para sesiones de usuarios
    'django.contrib.messages',  # Soporte para mensajes entre vistas
    'django.contrib.staticfiles',  # Manejo de archivos estáticos
    'app'  # Tu propia aplicación (se asume que la carpeta 'app' es una app dentro del proyecto)
]

# Ponemos Middleware para procesar las solicitudes HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Middleware de seguridad
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manejo de sesiones
    'django.middleware.common.CommonMiddleware',  # Middleware común
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware de autenticación
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware de mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protección contra clickjacking
]

# Configuramos las URLs del proyecto
ROOT_URLCONF = 'mysite.urls'  # Enlaza las URLs definidas a nivel de proyecto

# Configuramos plantillas (templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend para renderizar templates
        'DIRS': [BASE_DIR / 'templates'],  # Directorios que indican donde buscar los templates
        'APP_DIRS': True,  # Esto permite que se busquen templates dentro de las apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Contexto de debug
                'django.template.context_processors.request',  # Procesador
                'django.contrib.auth.context_processors.auth',  # Ñrocesador de autentificacion
                'django.contrib.messages.context_processors.messages',  # Procesador de mensajes
            ],
        },
    },
]

# Configuración del servidor WSGI (aplicaciones síncronas).
WSGI_APPLICATION = 'mysite.wsgi.application'


# Configuración de la base de datos
# Usamos SQLite por defecto en el entorno de desarrollo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos (SQLite).
        'NAME': BASE_DIR / 'db.sqlite3',  
    }
}


# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Configuración de internacionalización (i18n) y zonas horarias (tz)
LANGUAGE_CODE = 'en-us'  # Idioma por defecto del proyecto (inglés).
TIME_ZONE = 'UTC'  # Zona horaria por defecto (UTC).
USE_I18N = True  # Activa la internacionalización
USE_TZ = True  # Usa zonas horarias

# Archivos estáticos (CSS, JavaScript, imágenes)
STATIC_URL = 'static/'  # URL donde se sirven los archivos estáticos

# Definición del tipo de campo de clave primaria por defecto
# Campo para las claves primarias (BigAutoField, entero grande autoincremental).
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
