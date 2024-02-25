import unittest
from biseccion import biseccion
from newton import newton_raphson
from riemann import integracion_riemann
from trapecio import integracion_trapecio
from math import *

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: x**4 - 2*x - 5
        a = 1
        b = 3
        tol = 0.0001
        max_iter = 50
        self.assertEqual(biseccion.biseccion(a, b, tol, max_iter = 50),None)
        
class test_newton_raphson(unittest.TestCase):
    def test_newton_raphson(self):
        funcion= lambda x: x**4 - 2*x - 5 
        derivada_funcion = lambda x: 4*x**2 - 2 
        x0 = 2
        tol = 0.0001 
        max_iter = 50 
        self.assertEqual(newton.newton_raphson(funcion, derivada_funcion, x0, tol, max_iter),None)

class test_integracion_riemann(unittest.TestCase):
    def test_integracion_riemann(self):
        funcion= lambda x: x**4 - 2*x - 5
        a = 0 
        b = 2  
        n = 5 
        self.assertEqual(riemann.integracion_riemann(funcion, a, b, n),None)  
        
class test_integracion_trapecio(unittest.TestCase):
    def test_integracion_trapecio(self):
        funcion= lambda x: x**4 - 2*x - 5
        a = 0  
        b = 2  
        n = 5  
        self.assertEqual(trapecio.integracion_trapecio(funcion, a, b, n),None)                      
        
if __name__ == '__main__':
    unittest.main()