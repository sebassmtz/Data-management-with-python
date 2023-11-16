import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Ejercicio 1
print("-------------------Ejercicio 1-------------------------")

position = ['G','G','F','F','C','G','F','F','G','C']
serie_postion = pd.Series(position)
df_position = pd.DataFrame(serie_postion,columns=['position'])
frequency = df_position['position'].value_counts()
formated_frecuency = frequency.rename({'G': 'Guardia', 'F': 'Delantero', 'C': 'Centro'})
print(formated_frecuency)

print("------------Ejercicio 2 punto 2-------------------------")

url = "https://drive.google.com/uc?id=1jrD9j2zIzRFOcd48AiEwfS6re2uBdE1O"
df = pd.read_csv(url, encoding='latin-1')

#Tipo de variable de cada columna
# Cod_Div : Cualitativa ordinal
# Latitud: Cuantitaviva continua
# Longitud: Cuantittaviva continua
# Region: Cualitativa nominal
# Departamento: Cualitativa nominal
# Fecha: Cualitativa ordinal
# Hora: Cualitativa ordinal
# Temperatura: Cuantittaviva continua
# Velocidad del Viento: Cuantittaviva continua
# Dirección del Viento: Cualitativa ordinal
# Presión: Cuantittaviva continua
# Punto de Rocío: Cuantitaviva continua
# Cobertura total nubosa: Cuantittaviva continua
# Precipitación (mm/h): Cuantitaviva continua
# Probabilidad de Tormenta: Cuantitaviva continua
# Humedad: Cuantitaviva continua
# Pronóstico: Cualitativa nominal
print('-------------------Ejercicio 2 punto 3-------------------------')
# Calculando medidas de tendencia central
print("--- Media ---",df['Temperatura'].mean())
print("--- Mediana ---",df['Temperatura'].median())
print("--- Moda ---",df['Temperatura'].mode())

print('-------------------Ejercicio 2 punto 4-------------------------')

fig, ax = plt.subplots()
plt.boxplot(df['Temperatura'])
ax.set_title('Boxplot de Temperatura')
ax.set_ylabel('Temperatura')
plt.savefig('caja_de_bigotes_temperatura.png')
plt.show()
print('-------------------Ejercicio 2 punto 5-------------------------')

print('Cuartiles respecto a la variable Presión')
Q1 = df['Presión'].quantile(0.25)
print("Q1 ----> ", Q1)
Q2 = df['Presión'].quantile(0.50)
print("Q2 ---> ",Q2)
Q3 = df['Presión'].quantile(0.75)
print("Q3 ---->", Q3)

print("Rango intercuartil Respecto a la variable Presión:", Q3-Q1)

print("desviación estandar respecto a la variable Presión:", df['Presión'].std())

print("Varianza respecto a la variable Presión:", df['Presión'].var())

print("-------------------Ejercicio 2 punto 6-------------------------")

array_temperature = np.array(df['Temperatura'])
print(array_temperature)

print('-------------------Ejercicio 2 punto 7-------------------------')

print('Cuartiles respecto a la variable Temperatura')
Q1 = df['Temperatura'].quantile(0.25)
print("Q1 ----> ", Q1)
Q2 = df['Temperatura'].quantile(0.50)
print("Q2 ---> ",Q2)
Q3 = df['Temperatura'].quantile(0.75)
print("Q3 ---->", Q3)

print("Rango intercuartil Respecto a la variable Temperatura:", Q3-Q1)

print("desviación estandar respecto a la variable Temperatura:", df['Temperatura'].std())

print("Varianza respecto a la variable Temperatura:", df['Temperatura'].var())

print("-------------------Ejercicio 2 punto 8-------------------------")

frequent_temp = df['Temperatura'].mode().values[0]
print("Temperatura mas frecuente:", frequent_temp)

frequent_values = df[df['Temperatura'] == frequent_temp]['Temperatura']

rango = np.ptp(frequent_values)

print("Rango de la temperatura mas frecuente:", rango)

print("-------------------Ejercicio 2 punto 9-------------------------")

# Define el número de intervalos
num_intervals = 10

# Calcula el rango total de temperaturas
temp_range = df['Temperatura'].max() - df['Temperatura'].min()

# Calcula el tamaño de cada intervalo
interval_size = temp_range / num_intervals

# Almacena los rangos y las desviaciones estándar
ranges = []
std_devs = []

# Para cada intervalo
for i in range(num_intervals):
    # Calcula el rango de temperaturas para este intervalo
    lower_bound = df['Temperatura'].min() + i * interval_size
    upper_bound = lower_bound + interval_size
    
    # Selecciona las temperaturas dentro de este rango
    temp_in_range = df[(df['Temperatura'] >= lower_bound) & (df['Temperatura'] < upper_bound)]['Temperatura']
    
    # Calcula la desviación estándar de estas temperaturas
    std_dev = temp_in_range.std()
    
    # Almacena el rango y la desviación estándar
    ranges.append((lower_bound, upper_bound))
    std_devs.append(std_dev)

# Encuentra el rango con la mayor desviación estándar
max_std_dev_index = np.argmax(std_devs)
max_std_dev_range = ranges[max_std_dev_index]

print("Rango de temperatura con mayor dispersión:", max_std_dev_range)

print("-------------------Ejercicio 2 punto 10-------------------------")

# Calcula los cuartiles
q1 = df['Temperatura'].quantile(0.25)
q2 = df['Temperatura'].quantile(0.5)
q3 = df['Temperatura'].quantile(0.75)

# Almacena los rangos de cuartiles y las cuentas de datos
quartiles = [(df['Temperatura'].min(), q1), (q1, q2), (q2, q3), (q3, df['Temperatura'].max())]
counts = []

# Para cada cuartil
for lower_bound, upper_bound in quartiles:
    # Selecciona los datos dentro de este rango
    data_in_range = df[(df['Temperatura'] >= lower_bound) & (df['Temperatura'] < upper_bound)]['Temperatura']
    
    # Cuenta los datos seleccionados
    count = data_in_range.count()
    
    # Almacena la cuenta
    counts.append(count)

# Encuentra el cuartil con la mayor cantidad de datos
max_count_index = counts.index(max(counts))
max_count_quartile = quartiles[max_count_index]

print("Cuartil con la mayor cantidad de datos:", max_count_quartile)

print("-------------------Ejercicio 3 punto 11-------------------------")

fig, ax = plt.subplots()
plt.boxplot(df['Humedad'])
ax.set_title('Boxplot de Humedad')
ax.set_ylabel('Humedad')

plt.savefig('caja_de_bigotes_humedad.png')
plt.show()

print("-------------------Ejercicio 3 punto 12-------------------------")

print('Cuartiles respecto a la variable Temperatura')
Q1 = df['Temperatura'].quantile(0.25)
print("Q1 ----> ", Q1)
Q2 = df['Temperatura'].quantile(0.50)
print("Q2 ---> ",Q2)
Q3 = df['Temperatura'].quantile(0.75)
print("Q3 ---->", Q3)

print("Rango intercuartil Respecto a la variable Temperatura:", Q3-Q1)

print("desviación estandar respecto a la variable Temperatura:", df['Temperatura'].std())

print("Varianza respecto a la variable Temperatura:", df['Temperatura'].var())

print("-------------------Ejercicio 3 punto 13-------------------------")

array_humidity = np.array(df['Humedad'])    

print(array_humidity)

print("-------------------Ejercicio 3 punto 14-------------------------")

print('Cuartiles respecto a la variable Humedad')
Q1 = df['Humedad'].quantile(0.25)
print("Q1 ----> ", Q1)
Q2 = df['Humedad'].quantile(0.50)
print("Q2 ---> ",Q2)
Q3 = df['Humedad'].quantile(0.75)
print("Q3 ---->", Q3)

print("Rango intercuartil Respecto a la variable Humedad:", Q3-Q1)

print("desviación estandar respecto a la variable Humedad:", df['Humedad'].std())

print("Varianza respecto a la variable Humedad:", df['Humedad'].var())

print("-------------------Ejercicio 3 punto 15-------------------------")

frequent_temp = df['Humedad'].mode().values[0]
print("Humedad mas frecuente:", frequent_temp)

frequent_values = df[df['Humedad'] == frequent_temp]['Humedad']

rango = np.ptp(frequent_values)

print("Rango de la Humedad mas frecuente:", rango)

print("-------------------Ejercicio 3 punto 16-------------------------")

# Define el número de intervalos
num_intervals = 10

# Calcula el rango total de temperaturas
temp_range = df['Humedad'].max() - df['Humedad'].min()

# Calcula el tamaño de cada intervalo
interval_size = temp_range / num_intervals

# Almacena los rangos y las desviaciones estándar
ranges = []
std_devs = []

# Para cada intervalo
for i in range(num_intervals):
    # Calcula el rango de temperaturas para este intervalo
    lower_bound = df['Humedad'].min() + i * interval_size
    upper_bound = lower_bound + interval_size
    
    # Selecciona las temperaturas dentro de este rango
    temp_in_range = df[(df['Humedad'] >= lower_bound) & (df['Humedad'] < upper_bound)]['Humedad']
    
    # Calcula la desviación estándar de estas temperaturas
    std_dev = temp_in_range.std()
    
    # Almacena el rango y la desviación estándar
    ranges.append((lower_bound, upper_bound))
    std_devs.append(std_dev)

# Encuentra el rango con la mayor desviación estándar
max_std_dev_index = np.argmax(std_devs)
max_std_dev_range = ranges[max_std_dev_index]

print("Rango de Humedad con mayor dispersión:", max_std_dev_range)

print("-------------------Ejercicio 3 punto 17-------------------------")

# Calcula Q1, Q3 y IQR
Q1 = df['Velocidad del Viento'].quantile(0.25)
Q3 = df['Velocidad del Viento'].quantile(0.75)
IQR = Q3 - Q1

# Define los límites para los valores atípicos
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Selecciona los valores atípicos
outliers = df[(df['Velocidad del Viento'] < lower_bound) | (df['Velocidad del Viento'] > upper_bound)]['Velocidad del Viento']

print("Valores atípicos en 'Velocidad del Viento':", outliers)

print("-------------------Ejercicio 4 punto 18-------------------------")
forecast_frequencies = df['Pronóstico '].value_counts()
print("Frecuencias de los valores únicos en 'Pronóstico':")
print(forecast_frequencies)
