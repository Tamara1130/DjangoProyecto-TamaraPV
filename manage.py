#!/usr/bin/env python
"""Utilidad de línea de comandos de Django para tareas administrativas."""

import os  # Funciones para interactuar con el sistema operativo
import sys  # Da acceso a parámetros y funciones


def main():
    """Ejecuta tareas administrativas."""
    # Le indica a Django qué archivo de configuración debe usar (settings.py).
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    
    try:
        # Importa la función para ejecutar comandos administrativos
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Maneja el error si Django no está instalado o si hay problemas
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? "
            "¿Olvidaste activar un entorno virtual?"
        ) from exc
    
    # Ejecuta el comando usando línea de comandos
    execute_from_command_line(sys.argv)


# Este bloque asegura que el código solo se ejecutará si el archivo es llamado directamente
if __name__ == '__main__':
    main()

