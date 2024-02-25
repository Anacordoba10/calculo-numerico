from math import *

def integracion_trapecio(funcion, a, b, n):
    delta_x = (b - a) / n
    suma = 0.5 * (funcion(a) + funcion(b))  
    for i in range(1, n):
        suma += funcion(a + i * delta_x) 
    return delta_x * suma

def funcion(x):
    return x**4 - 2*x - 5  

if __name__ == '__main__':
    # Parámetros de entrada
    a = 0  
    b = 2  
    n = 5  

    # Llamada al método del trapecio
    area_aproximada = integracion_trapecio(funcion, a, b, n)

    print("El área aproximada bajo la curva es:", area_aproximada)

