from math import *

def biseccion(a, b, tol, max_iter = 50):
    if funcion(a) * funcion(b) >= 0:
        print("La función no cumple con el requisito del intervalo dado.")
        return None    
    Cont_inter = 0
    while True:
        c = (a + b) / 2.0
        if funcion(c) == 0 or (b - a) / 2.0 < tol:
            return c
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
        Cont_inter += 1
        if Cont_inter >= max_iter:
            print("Se ha alcanzado el número máximo de iteraciones.")
            return None
        
#Data del programa
        
def funcion(x):
    return x**4 - 2*x - 5
        
if __name__ == '__main__':
# Datos de entrada
    a = 1
    b = 3
    tol = 0.0001
    max_iter = 50

# Llamado de requerimiento para la funcion de biseccion
    raiz = biseccion(a, b, tol)

    if raiz is not None:
        print("La raíz aproximada es:", raiz)
