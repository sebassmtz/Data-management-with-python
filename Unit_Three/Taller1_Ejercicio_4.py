'''
Reversar un arreglo de numpy 1D, Sin usar funciones específicas de numpy:
Arreglo inicial [1 2 3 4 5 6]
Salida [6 5 4 3 2 1]
'''

import numpy as np

# Arreglo inicial
arr = np.array([1, 2, 3, 4, 5, 6])

# Revertir el arreglo sin usar funciones específicas de numpy
reversed_arr = arr[::-1]

# Imprimir el arreglo revertido
print(reversed_arr)