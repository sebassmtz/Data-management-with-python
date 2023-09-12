

#Realizar una funcion que reciba como parámetro la lista de los empleados. Mostrar la información
#de los empleados con el siguiente formato:
#formato 1: -> function formatListOne [x] Done
#empleado -- 1
#luis
#20
#55.6

#formato 2: -> function formatListTwo
#nombre empleado: Luis, Edad: 20, Peso: 55.6

#formato 3: -> function formatListThree
#Empleado_1:Luis, Edad: 20, Peso: 55.6
# Definir una lista de empleados como ejemplo
empleados = [
    {"nombre": "Luis", "edad": 20, "peso": 55.6},
    {"nombre": "Ana", "edad": 30, "peso": 65.2},
    {"nombre": "Juan", "edad": 25, "peso": 70.0}
]

# Formato 1: Función formatListOne
def formatListOne(empleados):
    for i, empleado in enumerate(empleados, start=1):
        print(f"Empleado -- {i}")
        print(empleado["nombre"])
        print(empleado["edad"])
        print(empleado["peso"])
        print()

# Formato 2: Función formatListTwo
def formatListTwo(empleados):
    for empleado in empleados:
        print(f"Nombre empleado: {empleado['nombre']}, Edad: {empleado['edad']}, Peso: {empleado['peso']}")

# Formato 3: Función formatListThree
def formatListThree(empleados):
    for i, empleado in enumerate(empleados, start=1):
        print(f"Empleado_{i}:{empleado['nombre']}, Edad: {empleado['edad']}, Peso: {empleado['peso']}")

# Llamar a las funciones con la lista de empleados
print("Formato 1:")
formatListOne(empleados)

print("\nFormato 2:")
formatListTwo(empleados)

print("\nFormato 3:")
formatListThree(empleados)