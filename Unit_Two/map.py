"""
Ejercicio
1. A aprtir de la siguiente lista de precios, utilice las funciones lambda y map, para aplicarle un aumento del 25% acada uno de los valeres
simpre y cuando no sobrepase los $270.000, en cuyo caso el valor queda como el original.
Lista de precios : 275.000 , 125.990 , 76.400, 110.900, 68.990, 185.900, 56.850, 352.950, 456.990, 30.990, 69.990, 206.350

"""

prices = [275.000 , 125.990 , 76.400, 110.900, 68.990, 185.900, 56.850, 352.950, 456.990,
30.990, 69.990, 206.350]

increased_prices = list(map(lambda x: x+(x*0.25) if x+(x*0.25)<270.000 else x, prices))

print(increased_prices)

