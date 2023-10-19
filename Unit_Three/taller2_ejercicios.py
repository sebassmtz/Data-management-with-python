import pandas as pd

# URL del archivo CSV en Google Drive
url = "https://drive.google.com/uc?export=download&id=1TJrHAQo-wrZe0zmbXGYehhDf1-58-kmK"

# Leer el archivo CSV
data = pd.read_csv(url)

# 1. Determine para cada una de las series la existencia de valores nulos
# 2. Remplace los valores nulos por 0
data.fillna('0', inplace=True)

# Mostrar información sobre el DataFrame
data.info()

# 3. Carge de nuevo el DataFrame original
datanew = pd.read_csv(url)

# 4. Elimine las filas que tienen valores nulos y observe la cantidad de filas resultantes
datanew.dropna(inplace=True)
datanew.info()

# 5. Observe el tipo de dato de cada una de las series del DataFrame
# ¿Por qué considera que la mayoría de series quedan con el tipo de dato Object?
print(datanew.dtypes)

# 6. Seleccione los empleados que pertenecen al Team Finance
finance_team = datanew[datanew.Team == 'Finance'][['First Name', 'Team']]
print(finance_team)

# 7. Crear un nuevo DataFrame con las series: First Name, Gender y Salary
# Muestre el registro con el índice 100 de ese nuevo DataFrame
newDataFrame = datanew[['First Name', 'Gender', 'Salary']]
print(newDataFrame.loc[100:100])

# 8. Ordene el DataFrame por salario, de forma ascendente y descendente
salarySortedAs = newDataFrame.sort_values(by=['Salary'], ascending=True, inplace=False)
salarySortedDes = newDataFrame.sort_values(by=['Salary'], ascending=False, inplace=False)
print(salarySortedAs)
print(salarySortedDes)

# 9. Muestre los empleados donde la serie salario es mayor a 49000 y menor a 50000
# Muestre las series nombre y salario del empleado
salaryQuery = newDataFrame[(newDataFrame.Salary > 49000) & (newDataFrame.Salary < 50000)][['First Name', 'Salary']]
print(salaryQuery)

# 10. Cambie el nombre de la serie First Name por Nombre
salaryQuery.rename(columns={'First Name': 'Nombre'}, inplace=True)
print(salaryQuery)

# 11. Cuente la cantidad de filas del item nueve (9)
print(salaryQuery.shape[0])