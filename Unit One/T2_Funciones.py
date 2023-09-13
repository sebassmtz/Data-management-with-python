"""
Funciones

1. Escribir una función que reciba un carácter y evalué si el valor ingresado, corresponde a una vocal o a una consonante. Cuando sea vocal
que retorne el valor booleano (TRUE).
2. Convertir el ejercicio de ecuación cuadrática a Función.

"""

from math import sqrt

def es_vocal(caracter):
    # Convierte el carácter a minúscula para que coincida con las vocales en minúscula.
    caracter = caracter.lower()
    # Verifica si el carácter es una vocal.
    return caracter in ('a', 'e', 'i', 'o', 'u')

# Prueba la función con un carácter.
char = 'a'
if es_vocal(char):
    print(f"'{char}' es una vocal.")
else:
    print(f"'{char}' es una consonante.")
    
def cuadratic(a, b, c):
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero")
    

    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        raise ValueError("El discriminante es negativo, no se pueden encontrar raíces reales")
    
    raiz_discriminante = sqrt(discriminante)
    
    x1 = (-b + raiz_discriminante) / (2*a)
    x2 = (-b - raiz_discriminante) / (2*a)
    
    return x1, x2

try:
    resultado = cuadratic(12, 6, -3)
    print("Las raíces son:", resultado)
except ValueError as e:
    print("Error:", e)