import matplotlib
matplotlib.use('Agg')  # Usa un backend sin GUI
import io
import random
import numpy as np
from matplotlib import pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render
import base64

def grafica_linea():
    """Generar una gráfica de líneas."""
    fig, ax = plt.subplots()
    x = range(10)
    y = [random.randint(1, 20) for _ in x]
    ax.plot(x, y, marker='o', label="Datos de línea")
    ax.set_title("Gráfica de Líneas")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()
    return fig

def grafica_barras():
    """Generar una gráfica de barras."""
    fig, ax = plt.subplots()
    categorias = ['A', 'B', 'C', 'D']
    valores = [random.randint(1, 20) for _ in categorias]
    ax.bar(categorias, valores, color='skyblue')
    ax.set_title("Gráfica de Barras")
    ax.set_xlabel("Categorías")
    ax.set_ylabel("Valores")
    return fig

def grafica_pastel():
    """Generar una gráfica de pastel."""
    fig, ax = plt.subplots()
    etiquetas = ['A', 'B', 'C', 'D']
    tamaños = [random.randint(1, 100) for _ in etiquetas]
    ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)
    ax.set_title("Gráfica de Pastel")
    return fig

def histograma():
    """Generar un histograma."""
    fig, ax = plt.subplots()
    datos = [random.gauss(0, 1) for _ in range(1000)]
    ax.hist(datos, bins=20, color='purple', edgecolor='black')
    ax.set_title("Histograma")
    return fig

def grafica_cajas():
    """Generar una gráfica de cajas (boxplot)."""
    fig, ax = plt.subplots()
    datos = [[random.gauss(0, 1) for _ in range(100)] for _ in range(4)]
    ax.boxplot(datos)
    ax.set_title("Gráfica de Cajas")
    return fig

def grafica_dispersion():
    """Generar una gráfica de dispersión con puntos definidos y una línea de tendencia."""
    # Generar algunos datos de ejemplo (con una relación lineal)
    np.random.seed(0)
    x = np.linspace(0, 10, 50)  # Generamos 50 puntos en el rango de 0 a 10
    y = 2 * x + 1 + np.random.randn(50)  # Relación lineal con algo de ruido

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Graficar los puntos dispersos
    ax.scatter(x, y, color='blue', label='Datos dispersos', s=100, alpha=0.7)  # s= tamaño de los puntos, alpha=transparencia

    # Agregar una línea de tendencia (ajuste lineal)
    coef = np.polyfit(x, y, 1)  # Ajuste lineal de grado 1
    poly = np.poly1d(coef)
    y_fit = poly(x)  # Valores ajustados
    ax.plot(x, y_fit, color='red', label='Línea de tendencia', linewidth=2)  # Línea de tendencia

    # Agregar título y etiquetas
    ax.set_title("Gráfica de Dispersión con Línea de Tendencia")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    # Agregar leyenda
    ax.legend()

    return fig

def obtener_imagen_grafica(fig):
    """Convertir la figura de matplotlib a una cadena Base64."""
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    imagen_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return imagen_base64

def random_graphs(request):  # Cambié el nombre de 'generar_graficas' a 'random_graphs'
    """Vista para generar y mostrar seis gráficas."""
    graficas = {
        'linea': obtener_imagen_grafica(grafica_linea()),
        'barras': obtener_imagen_grafica(grafica_barras()),
        'pastel': obtener_imagen_grafica(grafica_pastel()),
        'histograma': obtener_imagen_grafica(histograma()),
        'cajas': obtener_imagen_grafica(grafica_cajas()),
        'dispersión': obtener_imagen_grafica(grafica_dispersion()),
    }

    return render(request, 'app/random_graphs.html', {'graficas': graficas})
