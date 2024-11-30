# mysite/urls.py
# Importamos el módulo "path" de Django para manejar las rutas de la aplicación
from django.urls import path

# Se importa la vista "random_graphs" desde "app.views", vista la cual está encargada de generar y mostrar las gráficas
from app.views import random_graphs  

# Se definen las URLs de la aplicación y se asocian con las vistas
urlpatterns = [
    # Se define la URL "random-graphs/" que estará asociada con la vista "random_graphs"
    # Cuando se accede a esta URL, se ejecutará la función "random_graphs" en views.py
    path('random-graphs/', random_graphs, name='random_graphs'),
]

