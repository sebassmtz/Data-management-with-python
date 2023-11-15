from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot
from sklearn.preprocessing import LabelEncoder
from statsmodels.graphics.gofplots import qqplot
import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_tunja = pd.read_csv('./TUNJA_I_23.csv', sep=';', encoding='latin-1')
print(df_tunja.columns)

ndata_Tunja = df_tunja[['Temperatura', 'Velocidad del Viento', 'Dirección del Viento',
                        'Presión', 'Punto de Rocío', 'Cobertura total nubosa', 'Humedad']]
numeric_columns = ['Presión', 'Punto de Rocío']


for col in numeric_columns:
    ndata_Tunja[col] = ndata_Tunja[col].astype(
        str).str.replace(',', '.').astype(float)

correlation_matrix = ndata_Tunja.corr()
print(correlation_matrix)

# visualizar la matriz de correlación
corr = ndata_Tunja.corr()
corr.style.background_gradient(cmap='coolwarm')

df_tunja.plot.scatter(x=['Temperatura'], y=['Temperatura'])


df_tunja.plot.scatter(x=['Temperatura'], y=['Velocidad del Viento'])

df_tunja.plot.scatter(x=['Temperatura'], y=['Humedad'])

corr_df = ndata_Tunja.corr(method='pearson')
plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True)
# plt.show()


df_tunja.info()

# Mostrar los valores de la variable Pronóstico
df_tunja['Pronóstico ']

# Mostrar los valores únicos de la variable Pronóstico
df_tunja['Pronóstico '].unique().tolist()

# Agregar y renombrar la columna Pronóstico en el DataFrame.
ndata_Tunja.insert(
    7, "Pronostico", df_tunja['Pronóstico '], allow_duplicates=False)
ndata_Tunja
# %reset

# Imprimir los valores de las columnas del nuevo DataFrame
values = ndata_Tunja.values
values

# Aplicar la técnica LabelEcoder de la libreria Sklearn.

# integer encode direction
print('-----1---')
print(ndata_Tunja['Pronostico'].unique().tolist())
encoder = LabelEncoder()
values[:, 7] = encoder.fit_transform(values[:, 7])
print('-----2---')
Number_Pronostico = values[:, 7]
print(Number_Pronostico)
print('-----3---')
print(type(values))
np.unique(values[:, 7])

# print(Number_Pronostico)
serie_Number_Pronostico = pd.Series(Number_Pronostico)
# print(type(serie_Number_Pronostico))
df_numeros = pd.DataFrame(serie_Number_Pronostico)
df_resultante = pd.concat([ndata_Tunja, df_numeros], axis=1,)
ndata_Tunja.insert(8, "Number_Pronostico",
                   serie_Number_Pronostico, allow_duplicates=False)

print(df_resultante)

# specify columns to plot
groups = [0, 1, 2, 3, 4, 5, 6, 7]
# groups = [0, 1, 2, 3, 5, 6, 7]
i = 1
# plot each column
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, i)
    pyplot.plot(values[:, group])
    pyplot.title(ndata_Tunja.columns[group], y=0.5, loc='right')
    i += 1
# pyplot.show()

ndata_Tunja.dtypes

# Use técnicas de nomrmalización de datos y grafique para objeter un resultado similar al gráfico siguiente:


# Seleccionar las columnas numéricas que quieres normalizar
numeric_columns = ['Temperatura', 'Velocidad del Viento',
                   'Presión', 'Punto de Rocío', 'Cobertura total nubosa', 'Humedad']

# Crear un MinMaxScaler
scaler = MinMaxScaler()

# Normalizar los datos en el DataFrame
ndata_Tunja[numeric_columns] = scaler.fit_transform(
    ndata_Tunja[numeric_columns])

# Graficar los datos normalizados
ndata_Tunja[numeric_columns].plot(
    kind='density', subplots=True, layout=(3, 2), sharex=False)


# Seleccionar las columnas numéricas que quieres estandarizar
numeric_columns = ['Temperatura', 'Velocidad del Viento',
                   'Presión', 'Punto de Rocío', 'Cobertura total nubosa', 'Humedad']

# Crear un StandardScaler
scaler = StandardScaler()


ndata_Tunja[numeric_columns] = scaler.fit_transform(
    ndata_Tunja[numeric_columns])


# Ajusta esto si son diferentes columnas las que deseas graficar
groups = [0, 1, 2, 3, 4, 5, 6, 7]
i = 1

plt.figure(figsize=(10, 12))  # Ajusta el tamaño de la figura si es necesario
for group in groups:
    plt.subplot(len(groups), 1, i)
    plt.plot(ndata_Tunja.iloc[:, group])
    plt.title(ndata_Tunja.columns[group], y=0.5, loc='right')
    i += 1
plt.tight_layout()
plt.show()
