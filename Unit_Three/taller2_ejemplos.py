import pandas as pd
import numpy as nepe

'''
None and NaN
In Pandas missing data is represented by two value: None: None is a Python singleton object that is
often used for missing data in Python code. NaN : NaN (an acronym for Not a Number),
'''

df = pd.DataFrame({'col1': [1, 2, 3, nepe.nan],
                   'col2': [nepe.nan, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', None]})

print(df.fillna('0', inplace=True))
print(df)


'''
Series desde Diccionarios
'''

seleccionColombia = pd.Series(
    ['Ospina', 'Zapata', 'Falcao', 'Cuadrado', 'Rodriguez'],
    index=[1, 2, 9, 11, 10])  # the index can be disordered.
print(type(seleccionColombia))

# series with dictionaries
# series can be defined from dictionaries.

dict_selcol = {1: 'Ospina', 2: 'Zapata',
               9: 'Falcao', 11: 'Cuadrado', 10: 'Rodriguez'}

ser_selcol = pd.Series(dict_selcol)
print(ser_selcol)

print(len(ser_selcol.index))
print(len(ser_selcol.values))

print(len(ser_selcol[9]))

print(ser_selcol[ser_selcol >= 'O'])

ser_selcol.index.name = 'Num_Cam'  # you can name the index with this sentence
ser_selcol.name = 'Jugador'
print(ser_selcol)


'''
DataFrame
Un DataFrame es una estructura de datos que almacena la información como una tabla ordenada
por filas y columnas. Cada fila representa un objeto y cada columna la información correspondiente
a una característica de los objetos.
Un DataFrame también posee índices por cada fila, que pueden ser dados o generados
automáticamente. Cada columna del DataFrame es una [serie], donde el valor del índice
corresponde con los valores de índice que tiene el DataFrame.
Por medio de un diccionario vamos a crear un dataframe, donde las llaves son los nombres de las
columnas y los valores son las características.
Por ejemplo, para hacer un DataFrame con el equipo de fútbol anterior, pero agregando las series
de estatura y peso, se hará de la siguiente manera:
'''

dict_characteristics = {'apellido': ['Ospina', 'Zapata', 'Falcao', 'Cuadrado', 'Rodriguez'],
                        'altura': [183.0, 187.0, 177.0, 179.0, 180.0],
                        'peso': [80.0, 82.0, 72.0, 72.0, 75.0]}

selcol = pd.DataFrame(dict_characteristics, index=[1, 2, 9, 11, 10])
selcol.index.name = 'numerix'
print(selcol)

# access to the registers by index

print(selcol[selcol.altura == 187.0])
print(selcol[selcol.apellido == 'Zapata'])

# to add a new player (with dataframe.loc)

num = 56

characteristics = ['Vargas', 169.0, 70.0]
selcol.loc[num] = characteristics

print(selcol)

# to add a new player (with dataframe.add)

selcoldos = pd.DataFrame(
    {'apellido': 'sumama', 'altura': 169.5, 'peso': 89.5}, index=[8])

selcol = selcol.add(selcoldos)

print(selcol.keys())
print(selcol.dtypes)
print(selcol.values)

# delete column
# with drop
# inplace = True to make the delete permanent
selcol.drop('peso', axis=1, inplace=True)
print(selcol)

# with del
# you can also use

del selcol['altura']

print(selcol)

# delete rows

# array with the index of the row to be eliminated
selcol23 = selcol.drop([8, 56, 2])
print(selcol23)

print(selcol.columns)  # to get the columns of the dataframe
print(selcol.index)  # to get the indexs of the dataframes.

# sort a dataframe.
print('\n sort a dataframe \n')
newselcol = pd.DataFrame(dict_characteristics, index=[1, 2, 9, 11, 10])
print(newselcol)
print(newselcol.sort_index())
print(newselcol.sort_values(by=['altura'], ascending=False))


# /////////////

df = pd.DataFrame({'col 1': [1, 2, 3],
                   'col 2': [4, 5, 6],
                   'col 3': [7, 8, 9],
                   'Resume': [10, 11, 12]})
print(df)
# inplace =True permite hacer c
df.set_axis(['X', 'Y', 'Z', 'Resume'], axis=1)
print(df)  # en cambio de devolver un nuev
df.rename({'Z': 'W'}, axis=1, inplace=True)
print(df)
df.rename({1: 10}, inplace=True)
print(df)

df = pd.DataFrame([1, 2, 3])
print(df)
df.set_axis(['Temp'], axis=1)
print(df)
data = [['tom', 10], ['nick', 15], ['juli', 14]]
df = pd.DataFrame(data)  # df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)
df.set_axis(['Ciud', 'Temp'], axis=1)
print(df)
lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
lst2 = [11, 12, 13, 14, 15, 16, 17]
df = pd.DataFrame(list(zip(lst, lst2)),
                  columns=['Name', 'val'])
print(df)
