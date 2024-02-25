from math import *

def newton_raphson(funcion, derivada_funcion, x0, tol=1e-6, max_iter=50):
    cont_iter = 0
    while True:
        x1 = x0 - funcion(x0) / derivada_funcion(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        cont_iter += 1
        if cont_iter >= max_iter:
            print("Se ha alcanzado el número máximo de iteraciones.")
            return None
            
#Data del programa

def funcion(x):
    return x**4 - 2*x - 5
def derivada_funcion(x):
    return 4*x**2 - 2

if __name__ == '__main__':
# Data de entrada
    x0 = 2 
    tol = 0.0001 
    cont_iter = 0
    max_iter = 50  

    # Llamado al Método de Newton-Raphson
    raiz = newton_raphson(funcion, derivada_funcion, x0, tol, max_iter)

    if raiz is not None:
        print("La aproximada es:", raiz)
    
