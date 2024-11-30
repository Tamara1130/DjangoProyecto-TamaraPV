# Usamos un backend sin GUI (genera las graficas sin necesidad de una interfaz gráfica)
import matplotlib
matplotlib.use('Agg')

# Importamos lo necesario para generar gráficas y manejarlas
import io
import random
import numpy as np
from matplotlib import pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render
import base64

# Función para crear una gráfica de líneas
def grafica_linea():
    """Genera una gráfica de líneas con datos aleatorios."""
    fig, ax = plt.subplots()
    x = range(10)  # Datos del eje X
    y = [random.randint(1, 20) for _ in x]  # Datos aleatorios para el eje Y
    ax.plot(x, y, marker='o', label="Datos de línea")  # Hacemos la línea
    ax.set_title("Gráfica de Líneas")  # Título
    ax.set_xlabel("Eje X")  # Etiqueta eje X
    ax.set_ylabel("Eje Y")  # Etiqueta eje Y
    ax.legend()  # Ponemos la leyenda
    return fig

# Función para crear una gráfica de barras
def grafica_barras():
    """Genera una gráfica de barras con datos aleatorios."""
    fig, ax = plt.subplots()
    categorias = ['A', 'B', 'C', 'D']  # Categorías en el eje X
    valores = [random.randint(1, 20) for _ in categorias]  # Valores aleatorios para las barras
    ax.bar(categorias, valores, color='skyblue')  # Creamos las barras
    ax.set_title("Gráfica de Barras")  # Título
    ax.set_xlabel("Categorías")  # Etiqueta eje X
    ax.set_ylabel("Valores")  # Etiqueta eje Y
    return fig

# Función para crear una gráfica de pastel
def grafica_pastel():
    """Genera una gráfica de pastel con datos aleatorios."""
    fig, ax = plt.subplots()
    etiquetas = ['A', 'B', 'C', 'D']  # Etiquetas
    tamaños = [random.randint(1, 100) for _ in etiquetas]  # Tamaños aleatorios para las secciones
    ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)  # Hacemos el pastel
    ax.set_title("Gráfica de Pastel")  # Título
    return fig

# Función para generar un histograma con datos aleatorios
def histograma():
    """Genera un histograma con datos aleatorios de una distribución gaussiana."""
    fig, ax = plt.subplots()
    datos = [random.gauss(0, 1) for _ in range(1000)]  # Datos aleatorios
    ax.hist(datos, bins=20, color='purple', edgecolor='black')  # Creamos el histograma
    ax.set_title("Histograma")  # Título
    return fig

# Función para crear una gráfica de cajas (boxplot)
def grafica_cajas():
    """Genera una gráfica de cajas con datos aleatorios."""
    fig, ax = plt.subplots()
    datos = [[random.gauss(0, 1) for _ in range(100)] for _ in range(4)]  # Datos aleatorios
    ax.boxplot(datos)  # Hacemos el boxplot
    ax.set_title("Gráfica de Cajas")  # Título
    return fig

# Función para generar una gráfica de dispersión con puntos y línea de tendencia
def grafica_dispersion():
    """Genera una gráfica de dispersión con una línea de tendencia."""
    np.random.seed(0)  # Semilla para reproducibilidad para que sean consistentes entre ejecuciones
    x = np.linspace(0, 10, 50)  # Generamos 50 puntos para el eje X
    y = 2 * x + 1 + np.random.randn(50)  

    fig, ax = plt.subplots()

    # Creamos los puntos de dispersión
    ax.scatter(x, y, color='blue', label='Datos dispersos', s=100, alpha=0.7)

    # Ajustamos una línea de tendencia
    coef = np.polyfit(x, y, 1)  # Ajuste lineal de los datos
    poly = np.poly1d(coef)
    y_fit = poly(x)  # Valores ajustados para la línea
    ax.plot(x, y_fit, color='red', label='Línea de tendencia', linewidth=2)  # Creamos la línea

    # Título y etiquetas
    ax.set_title("Gráfica de Dispersión con Línea de Tendencia")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    # Leyenda
    ax.legend()

    return fig

# Función para convertir las gráficas a formato Base64 (la Base64 convierte datos binarios en un texto legible)
def obtener_imagen_grafica(fig):
    """Convierte la gráfica a una cadena Base64 para renderizarla en HTML."""
    buf = io.BytesIO()  # Creamos un buffer en memoria (el buffer es un archivo virtual y puedes deshacerte de él cuando ya no lo ocupes)
    fig.savefig(buf, format='png')  # Guardamos la figura en el buffer en formato PNG
    buf.seek(0)  # Volvemos al inicio del buffer
    imagen_base64 = base64.b64encode(buf.read()).decode('utf-8')  # Pasamos a Base64
    plt.close(fig)  # Cerramos la figura para liberar recursos
    return imagen_base64

# Vista principal para generar las gráficas y enviarlas a template
def random_graphs(request):  
    """Genera y muestra las seis gráficas aleatorias."""
    graficas = {
        'linea': obtener_imagen_grafica(grafica_linea()),  # Gráfica de líneas
        'barras': obtener_imagen_grafica(grafica_barras()),  # Gráfica de barras
        'pastel': obtener_imagen_grafica(grafica_pastel()),  # Gráfica de pastel
        'histograma': obtener_imagen_grafica(histograma()),  # Histograma
        'cajas': obtener_imagen_grafica(grafica_cajas()),  # Boxplot
        'dispersión': obtener_imagen_grafica(grafica_dispersion()),  # Gráfica de dispersión
    }

    # Enviamos las gráficas al template "random_graphs.html"
    return render(request, 'app/random_graphs.html', {'graficas': graficas})

