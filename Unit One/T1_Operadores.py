from math import sqrt

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