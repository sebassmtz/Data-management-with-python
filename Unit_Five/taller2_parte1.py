from statsmodels.graphics.gofplots import qqplot
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_tunja = pd.read_csv('./TUNJA_I_23.csv', sep=';', encoding='latin-1')
print(df_tunja.columns)

# # Escriba su código aqui. con la funcion describe

print(df_tunja.describe())

# Identifique valores atípicos de la variable Velocidad del Viento Utilice un gráfica cajas o bigotes
plt.figure(figsize=(8, 6))
plt.boxplot(df_tunja['Velocidad del Viento'])
plt.title('Boxplot de Velocidad del Viento')
plt.ylabel('Velocidad del Viento')
# plt.show()

# Otra forma de verificar gráficamente valores atípicos
Velocidad_Viento = df_tunja['Velocidad del Viento']
velocidad_unique, counts = np.unique(Velocidad_Viento, return_counts=True)
sizes = counts*100
colors = ['blue']*len(velocidad_unique)
colors[-1] = 'red'
plt.axhline(1, color='black', linestyle='--')
plt.scatter(velocidad_unique, np.ones(
    len(velocidad_unique)), s=sizes, color=colors)
plt.yticks([])
plt.show()

# Observe los valores de la variable velocidad del viento en en array

print("Valores de la variable velocidad del viento en un array")
df_vviento = df_tunja['Velocidad del Viento']
print(type(df_vviento))
df_vviento_array = np.array(df_vviento)
print(np.sort(df_vviento_array, axis=None))

# otra forma de graficar los valores de la variable
Hora = range(1, 77)
y = df_tunja['Velocidad del Viento']
fig = px.scatter(x=Hora, y=y)
fig.update_layout(title='Gráfico de dispersión de Velocidad del Viento vs Hora',
                  xaxis_title='Velocidad del Viento',
                  yaxis_title='Hora')
fig.show()


# Graficar el histograma que representa los valores de la variable, velocidad del viento.

# Represento el histograma
plt.figure(figsize=(8, 6))
plt.hist(df_tunja['Velocidad del Viento'])
plt.title('Histograma Velocidad del Viento')
plt.show()

# 1. Represente los valores de la variable temperatura en un grafico de cajas o bigotes. Analice elcomportamiento de la variable.

plt.figure(figsize=(8, 6))
plt.boxplot(df_tunja['Temperatura'])
plt.title('Boxplot de Temperatura')
plt.ylabel('Temperatura')
plt.show()

# 2. Observe los valores de la variable temperatura en un array
print("Valores de la variable temperatura en un array")
temperatura_array = df_tunja['Temperatura'].values
print(temperatura_array)

# 3. Grafique los datos de la variable temperatura en gráfico px.scatter
# Gráfico de dispersión de Temperatura con Plotly Express
fig = px.scatter(df_tunja, y='Temperatura')
fig.update_layout(title='Gráfico de dispersión de la variable Temperatura',
                  xaxis_title='Índice de Muestra',
                  yaxis_title='Temperatura')
fig.show()

# 4. Graficar el histograma que representa los valores de la variable, Temperatura.
# Histograma de Temperatura
plt.figure(figsize=(8, 6))
plt.hist(df_tunja['Temperatura'])
plt.title('Histograma Temperatura')
plt.show()


# Gráfico QQ de Temperatura
plt.figure(figsize=(8, 6))
qqplot(df_tunja['Temperatura'], line='s')
plt.show()

"""
Analizar el comportamiento de la temperatura en el transcurso del día 01 de abril de 2023.
Ubicar hora de menor temperatura y hora de mayor temperatura
Posibles datos atípicos.
"""

df_temperatura = df_tunja[df_tunja.Fecha ==
                          '2023-04-01'][['Fecha', 'Hora', 'Temperatura']]
df_temperatura

print(df_temperatura.dtypes)

# 5. Genere un gráfico gráfico tipo px.scatter a partir de los datos anteriores

df_temperatura['Hora'] = pd.to_datetime(df_temperatura['Hora'])

fig = px.scatter(df_temperatura, x='Hora', y='Temperatura',
                 title='Gráfico de dispersión de Temperatura para el 1 de abril de 2023')
fig.update_xaxes(title='Hora')
fig.update_yaxes(title='Temperatura')
fig.show()

# Posibles datos atípicos.
# Comprender el codigo implementado
temp_filt = df_tunja[(df_tunja['Fecha'] == '2023-04-01')
                     ][['Fecha', 'Hora', 'Temperatura']]
# df_tunja.dtypes
# temp_filt
tempList = temp_filt['Temperatura']
p25t = tempList.quantile(0.25)
p75t = tempList.quantile(0.75)
rangoInter = p75t-p25t


def falsosPosi(dato1, dato2):
    return dato1 if (dato1-dato2) < rangoInter else None


listaT = list(np.sort(np.array(temp_filt['Temperatura']))[::-1])
listaLimpia = list(map(lambda t: falsosPosi(t[0], t[1]), zip(
    listaT, listaT[1:])))  # elimino los datos inconsistentes
res = [i for i in listaLimpia if i is not None]
pdRes = pd.DataFrame(res)
vlrMin = pdRes.min().iat[0]
vlrMax = pdRes.max().iat[0]
print('Valor Minimo:{}\nValor Maximo:{}'.format(vlrMin, vlrMax))

print(min(tempList))
print(max(tempList))

# Verificar existencia de Valores Nulos o faltantes. Decidir que hacer con esos valores: remplazarlos, borrarlos o realizar Imputación.

df_tunja.info()

#Calcular nuevamente la media o promedio de la variable Presión
df_tunja.Presión.mean()