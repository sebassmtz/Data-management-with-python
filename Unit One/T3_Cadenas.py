# Definir la cadena mostrada en la imagen anterior en una variable.
# Mostrar los caracteres de los indices 4 y 11
asignatura="Gestion de Datos"
type(asignatura)

print(asignatura[4], asignatura[11])


# Utilizar un metodo para dividir una frase en palabras. Use método split
# Ejemplo: "Gestión de Datos" Salida: ['Gestión', 'de', 'Datos']
frase = "Gestión de Datos"
palabras = frase.split()

print(palabras)


'''
Realice una función
Almacenar una cadena de caracteres en una variable y evaluar cuantas vocales tiene la frase.
Ejemplo: "Gestión de Datos"
Salida: a --> 1 e ---> 1 i --- > 1 o ---> 2 u ---> 0 Otras letras --->
'''
def es_vocal(caracter):
    # Convierte el carácter a minúscula para que coincida con las vocales en minúscula.
    caracter = caracter.lower()
    # Verifica si el carácter es una vocal.
    return caracter in ('a', 'e', 'i', 'o', 'u')

def contar_vocales(phrase):
    # Inicializa contadores para cada vocal.
    a = e = letteri = o = u = 0
    
    # Convierte la frase a minúscula para que coincida con las vocales en minúscula.
    phrase = phrase.lower()
    
    # Itera sobre los caracteres de la frase y cuenta las vocales.
    for caracter in phrase:
        if es_vocal(caracter):
            if caracter == 'a':
                a += 1
            elif caracter == 'e':
                e += 1
            elif caracter == 'i':
                letteri += 1
            elif caracter == 'o':
                o += 1
            elif caracter == 'u':
                u += 1
    
    return {'a': a, 'e': e, 'i': letteri, 'o': o, 'u': u}

def imprimir_contador_de_vocales(frase, contador):
    print(f'La frase "{frase}" tiene:', end=' ')
    for vocal, cantidad in contador.items():
        print(f'{vocal}-> {cantidad}', end=' ')
    print()

frase = 'gestion de datos'
contador_de_vocales = contar_vocales(frase)
imprimir_contador_de_vocales(frase, contador_de_vocales)