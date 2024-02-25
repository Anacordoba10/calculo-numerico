from math import *

def integracion_riemann(funcion, a, b, n):
    delta_x = (b - a) / n
    suma = 0
    for i in range(n):
        x_i = a + i * delta_x
        suma += funcion(x_i) * delta_x
    return suma

# Colocamos la función a aproximar en el área bajo la curva
def funcion(x):
    return x**4 - 2*x - 5  

if __name__ == '__main__':
    # Parámetros de entrada
    a = 0 
    b = 2  
    n = 5 

    # Llamada al método de la suma de Riemann
    area_aproximada = integracion_riemann(funcion, a, b, n)

    print("El área aproximada es:", area_aproximada)

