# mysite/urls.py
# Importamos el módulo "path" de Django para manejar las rutas de la aplicación
from django.urls import path

# Importamos la vista "random_graphs" desde "app.views"
from app.views import random_graphs

# Definimos las URLs de la aplicación y las asociamos con las vistas correspondientes
urlpatterns = [
    # URL raíz, asociada con la vista "random_graphs"
    path('', random_graphs, name='random_graphs'),  
    
    # URL específica para acceder a las gráficas, si se quiere usar un nombre más descriptivo
    path('random-graphs/', random_graphs, name='random_graphs'),
]

