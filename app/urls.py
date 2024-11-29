# mysite/urls.py
from django.urls import path
from app.views import random_graphs  # Asegúrate de que el nombre coincida

urlpatterns = [
    path('random-graphs/', random_graphs, name='random_graphs'),
]
