'''
Ejercicio 2 Por medio de ejemplos identificar y definir el uso de las siguientes funciones de numpy:

bitcount() y bitcount().argmax()
hstack, vstack y dstack
tolist
comparison.all
flipud
isin
flatten
unique
asarray
where

'''
import numpy as np

# numpy.bitcount() se utiliza para contar el número de bits activos (1) en una representación binaria de un número o matriz de números.

# binary_num = np.array([3, 5, 6])
# bit_count = np.bitcount(binary_num)
# print(bit_count)
# # Output: [2 2 2]

# # numpy.bitcount().argmax() se usa para encontrar el índice del elemento con el recuento máximo de bits activos en una matriz de números.

# binary_nums = np.array([3, 5, 6])
# bit_counts = np.bitcount(binary_nums)
# index_max_bits = bit_counts.argmax()
# print(index_max_bits)
# # Output: 0 (El número 3 tiene el mayor recuento de bits activos, que es 2)

'''
numpy.hstack() se utiliza para apilar matrices horizontalmente (a lo largo de las columnas).
numpy.vstack() se utiliza para apilar matrices verticalmente (a lo largo de las filas).
numpy.dstack() se utiliza para apilar matrices a lo largo de una tercera dimensión (profundidad).
'''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

hstacked = np.hstack((arr1, arr2))
vstacked = np.vstack((arr1, arr2))
dstacked = np.dstack((arr1, arr2))

print(hstacked)
print(vstacked)
print(dstacked)

# numpy.tolist() se utiliza para convertir un arreglo NumPy en una lista de Python.

arr = np.array([1, 2, 3])
arr_list = arr.tolist()
print(arr_list)
# Output: [1, 2, 3]

# numpy.all() se usa para verificar si todos los elementos de un arreglo NumPy cumplen una condición dada.

arr = np.array([1, 2, 3, 4, 5])
all_greater_than_zero = (arr > 0).all()
print(all_greater_than_zero)
# Output: True

# numpy.flipud() se utiliza para invertir un arreglo a lo largo del eje vertical.

arr = np.array([[1, 2, 3], [4, 5, 6]])
flipped_arr = np.flipud(arr)
print(flipped_arr)

# numpy.isin() se utiliza para verificar si los elementos de un arreglo están presentes en otro arreglo.

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 4, 6])
result = np.isin(arr1, arr2)
print(result)
# Output: [False  True False  True False]

# numpy.flatten() se utiliza para convertir un arreglo multidimensional en un arreglo unidimensional.

arr = np.array([[1, 2, 3], [4, 5, 6]])
flattened_arr = arr.flatten()
print(flattened_arr)

# numpy.unique() se utiliza para obtener los elementos únicos de un arreglo, eliminando duplicados.

arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique_elements = np.unique(arr)
print(unique_elements)
# Output: [1 2 3 4 5]

# numpy.asarray() se utiliza para convertir una secuencia (como lista o tupla) en un arreglo NumPy.

my_list = [1, 2, 3]
arr = np.asarray(my_list)
print(arr)

# numpy.where() se utiliza para encontrar los índices donde se cumple una condición dada en un arreglo y devuelve esos índices.

arr = np.array([1, 2, 3, 4, 5])
indices = np.where(arr > 3)
print(indices)
# Output: (array([3, 4]),)


