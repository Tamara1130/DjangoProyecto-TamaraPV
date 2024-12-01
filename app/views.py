# Usamos un backend sin GUI (genera las gráficas sin necesidad de una interfaz gráfica)
import matplotlib
matplotlib.use('Agg')

# Importamos lo necesario para generar gráficas y manejarlas
import io
import numpy as np
from matplotlib import pyplot as plt
from django.shortcuts import render
import base64


# Función para crear una gráfica de líneas
def grafica_linea():
    """Genera una gráfica de líneas basada en las ventas de zapatos."""
    fig, ax = plt.subplots()
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']  # Meses del año
    ventas = [50, 80, 45, 90, 120, 150]  # Ventas de zapatos
    ax.plot(meses, ventas, marker='o', label="Ventas de Zapatos", color='blue')  # Línea con los datos
    ax.set_title("Ventas Mensuales de Zapatos")  # Título
    ax.set_xlabel("Meses")  # Etiqueta eje X
    ax.set_ylabel("Ventas")  # Etiqueta eje Y
    ax.legend()  # Leyenda
    return fig


# Función para crear una gráfica de barras
def grafica_barras():
    """Genera una gráfica de barras sobre el índice de empleabilidad por estado."""
    fig, ax = plt.subplots()
    estados = ['Aguascalientes', 'Jalisco', 'CDMX', 'Nuevo León']  # Estados
    empleabilidad = [85, 78, 92, 88]  # Índice de empleabilidad (en porcentaje)
    ax.bar(estados, empleabilidad, color='green')  # Barras
    ax.set_title("Índice de Empleabilidad por Estado")  # Título
    ax.set_xlabel("Estados")  # Etiqueta eje X
    ax.set_ylabel("Porcentaje de Empleabilidad")  # Etiqueta eje Y
    return fig


# Función para crear una gráfica de pastel
def grafica_pastel():
    """Genera una gráfica de pastel sobre el estado de calificaciones de un grupo."""
    fig, ax = plt.subplots()
    categorias = ['Aprobados', 'Reprobados', 'Excelentes']  # Categorías
    porcentajes = [50, 20, 30]  # Porcentajes
    ax.pie(porcentajes, labels=categorias, autopct='%1.1f%%', startangle=90, colors=['yellow', 'red', 'green'])
    ax.set_title("Estado de Calificaciones de un Grupo")  # Título
    return fig


# Función para generar un histograma
def histograma():
    """Genera un histograma sobre la tasa de natalidad por región."""
    fig, ax = plt.subplots()
    regiones = ['Norte', 'Centro', 'Sur', 'Occidente']  # Regiones
    tasas = [12, 15, 10, 14]  # Tasa de natalidad (nacimientos por cada mil habitantes)
    ax.bar(regiones, tasas, color='orange', edgecolor='black')  # Histograma como barras
    ax.set_title("Tasa de Natalidad por Región")  # Título
    ax.set_xlabel("Regiones")  # Etiqueta eje X
    ax.set_ylabel("Tasa de Natalidad (por cada mil)")  # Etiqueta eje Y
    return fig


# Función para crear una gráfica de cajas (boxplot)
def grafica_cajas():
    """Genera una gráfica de cajas sobre la producción mensual en fábricas."""
    fig, ax = plt.subplots()
    datos = [
        [200, 210, 220, 205],  # Producción fábrica A
        [190, 195, 200, 185],  # Producción fábrica B
        [250, 260, 270, 255],  # Producción fábrica C
    ]
    ax.boxplot(datos, labels=['Fábrica A', 'Fábrica B', 'Fábrica C'])
    ax.set_title("Producción Mensual por Fábrica")  # Título
    ax.set_ylabel("Unidades Producidas")  # Etiqueta eje Y
    return fig


# Función para generar una gráfica de dispersión
def grafica_dispersion():
    """Genera una gráfica de dispersión con una línea de tendencia sobre los resultados de ventas anuales."""
    np.random.seed(0)
    años = [2018, 2019, 2020, 2021, 2022]  # Años
    ventas = [500, 600, 700, 650, 750]  # Ventas en miles
    variaciones = [5, -10, 15, -5, 10]  # Variaciones (ruido aleatorio)
    ventas_ajustadas = [v + np.random.choice(variaciones) for v in ventas]

    # Ajustar los datos a un modelo lineal
    coeficientes = np.polyfit(años, ventas_ajustadas, 1)  # Ajuste lineal (grado 1)
    linea_ajustada = np.poly1d(coeficientes)  # Generar la línea ajustada
    y_ajustada = linea_ajustada(años)  # Valores de la línea para cada punto de X (años)

    # Crear la gráfica
    fig, ax = plt.subplots()
    ax.scatter(años, ventas_ajustadas, color='purple', label="Ventas", s=100)  # Puntos de dispersión
    ax.plot(años, y_ajustada, color='red', label="Línea de tendencia", linewidth=2)  # Línea ajustada
    ax.set_title("Resultados de Ventas Anuales")
    ax.set_xlabel("Año")
    ax.set_ylabel("Ventas (en miles)")
    ax.legend()  # Leyenda para identificar los elementos de la gráfica
    return fig



# Función para convertir las gráficas a formato Base64
def obtener_imagen_grafica(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    imagen_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return imagen_base64


# Vista principal para generar las gráficas
def random_graphs(request):
    """Genera y muestra gráficas basadas en datos específicos."""
    graficas = {
        'linea': obtener_imagen_grafica(grafica_linea()),
        'barras': obtener_imagen_grafica(grafica_barras()),
        'pastel': obtener_imagen_grafica(grafica_pastel()),
        'histograma': obtener_imagen_grafica(histograma()),
        'cajas': obtener_imagen_grafica(grafica_cajas()),
        'dispersión': obtener_imagen_grafica(grafica_dispersion()),
    }
    return render(request, 'app/random_graphs.html', {'graficas': graficas})

