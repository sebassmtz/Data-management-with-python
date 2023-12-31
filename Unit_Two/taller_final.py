from functools import reduce
#Taller unidad 2

#1. pedidos de libros


pedidos1 = [ ["45", "Nacho Lee, Pedro Cardenas", 5, 32.50],  
            ["87", "Urbanidad de Carreño, Juan Carreño", 4, 60.20],  
            ["72", "Aprenda a jugar dados en dos días, Ana Parra", 4,22.80], 
            ["81", "En Vendedor de Sueños, Benito Hernandez", 4, 15.60]] 

#generar una lista de tuplas con el numero de pedio y total de precio
#cada tupla debe incrementarse en 15 pesos si el valor del pedido es inferior a 80 pesos

salida = list(map((lambda x: (x[0], x[1]+15) if x[1] < 80 else (x[0], x[1])), ((y[0], y[2]*y[3]) for y in pedidos1)))
print('lista de tuplas con numero de pedido y costo total aplicando la restriccion')
print(salida)

#2. pedidos 2

pedidos2 = [ [1, ("45", 3, 12.5),   ("27",15,20.5), ("74", 10, 38.5)],   
            [2, ("45", 10, 12.5),  ("74", 11, 38.5)],  
            [3, ("45", 2, 12.5),  ("27", 1, 20.5)],  
            [4, ("31", 6, 14.0),   ("30",9,27.0),  ("100", 15, 40.5)],  
            [5, ("31", 5, 14.0),   ("30",12,27.0), ("27", 4, 20.5)]] 

def calculate_order_total(order):
    order_number, *items = order
    total_price = sum(item[1] * item[2] for item in items)
    return [order_number, total_price]

def getPrice(pedidosList):
    return [calculate_order_total(order) for order in pedidosList]

prices = getPrice(pedidos2)
salida = list(map(lambda x: [x[0], x[1]+15] if x[1] < 80 else [x[0], x[1]], prices))
print('lista de listas con codigo de pedido y valor total de pedido')
print(salida)


