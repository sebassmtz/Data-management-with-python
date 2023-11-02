import pandas as pd
import numpy as np

df_emp = pd.read_csv('./employees.csv', sep=';', encoding='UTF-8')
print(df_emp.columns)

#
# 1. Mostrar los empleados que son del departamento 50 y tienen un salario igual o superior a 4000. Proyectar
# nombre, apellido, salario y departamento

department_50_high_salary = df_emp[(df_emp['DEPARTMENT_ID'] == 50) & (df_emp['SALARY'] >= 4000)]
selected_columns = department_50_high_salary[['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT_ID']]
print(selected_columns)
print('*' * 50)

# 2. Cuál es el cargo (Job_Id) de empleados que tengan nombre Alexander. Mostrar nombre, apellido y codigo de trabajo.

print(df_emp.query("FIRST_NAME == 'Alexander'")[['JOB_ID', 'FIRST_NAME', 'LAST_NAME']])
print('*' * 50)

# 3. Seleccionar los empleados cuyo salario es igual al mínimo salario de la compañia.

minsalary = min(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == minsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])
print('*' * 50)

# 4. Seleccionar los empleados cuyo salario es mayor al salario promedio de la compañia.

meansalary = np.mean(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY > meansalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])
print('*' * 50)

# 5. . Listar el empleado con el salario mas alto de la compañia

maxsalary = max(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == maxsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])
print('*' * 50)


# 6. Consultar la cantidad de empleados que pertenecen a cada departamento.

print(df_emp.groupby('DEPARTMENT_ID').size())
print('*' * 50)

# 7. Determinar para cada departamento cual es el minímo salario.

print(df_emp.groupby('DEPARTMENT_ID')['SALARY'].min())
print('*' * 50)

# 8. Determinar para cada departamento cual es el máximo salario.

print(df_emp.groupby('DEPARTMENT_ID')['SALARY'].max())
print('*' * 50)

# 9. Cuales son los 5 cargos más comunes. Probar con la fucnión value_counts()

print(df_emp['JOB_ID'].value_counts().rank(method='max').head(5))
print('*' * 50)

# 10. Cuales son los 5 departamentos con más empleados (más comunes)

print(df_emp[['DEPARTMENT_ID']].value_counts().rank(method='max').head(5))
print('*' * 50)

# 11. Lista de empleados que el apellido contenga las letras "man". Posiblemente es necesario utilizar funciones como: contains, lower y upper.
print(df_emp[df_emp.LAST_NAME.str.contains('[manMAN]', regex=True)]['LAST_NAME'])
print('*' * 50)

# 12. Mostrar los empleados, donde el apellido contenga una letra H o la letra k.
print(df_emp[df_emp.LAST_NAME.str.contains('[hkHK]', regex=True)]['LAST_NAME'])
print('*' * 50)

# 13. Mostrar los empleados, donde el apellido contenga una letra h, enseguida 2 caracteres cualquiera y luego la letra o.

print(df_emp[df_emp.LAST_NAME.str.contains("h..o", regex=True)]['LAST_NAME'])
print('*' * 50)

# 14. Mostrar los empleados donde el apellido finalilice con la letra g

print(df_emp[df_emp.LAST_NAME.str.contains("g$", regex=True)]['LAST_NAME'])
print('*' * 50)

# 15. Nombre del empleado con mayor salario de la organización

maxsalary = max(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == maxsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])
print('*' * 50)

# 16. Ordene los salarios de los empleados de forma descendente. Utilice función sort_values

print(df_emp[['FIRST_NAME', 'LAST_NAME', 'SALARY']].sort_values(by=['SALARY'], ascending=False))
print('*' * 50)

# 17. Empleados cuyo salario es mayor o igual a 13500 y menor o igual a 17000. Mostrar las columnas FIRST_NAME, LAST_NAME, JOB_ID,
# SALARY.

print(df_emp.query('SALARY >= 13500 and SALARY <= 17000')[['FIRST_NAME', 'LAST_NAME', 'JOB_ID', 'SALARY']])
print('*' * 50)
#18. Empleados que pertenecen a los departamentos: 10, 20, 40 y 70. Mostrar solamente las columnas DEPARTMENT_ID,FIRST_NAME. Utilice
# la función isin

print(df_emp[df_emp.DEPARTMENT_ID.isin([10, 20, 40, 70])][['FIRST_NAME', 'DEPARTMENT_ID']])
print('*' * 50)

# 19. Empleados que NO pertenecen a los departamentos: 10, 20, 40 y 70. Mostrar solamente las columnas DEPARTMENT_ID,FIRST_NAME.
# Utilice la negación ~

print(df_emp[~df_emp.DEPARTMENT_ID.isin([10, 20, 40, 70])][['FIRST_NAME', 'DEPARTMENT_ID']])
print('*' * 50)

# 20. Identifique la Razón por la que aparecen en el DataFrame resultado (df_unido) MANAGER_ID_x y MANAGER_ID_y, y el por qué no tienen la
# misma información

df_dep = pd.read_csv('./departments.csv', sep=';', encoding='UTF-8')
print(df_dep.columns)

df_unido = pd.merge(df_emp, df_dep, on='DEPARTMENT_ID')

print(df_unido.columns)

print(df_emp['MANAGER_ID'].head(5))
print(df_dep['MANAGER_ID'].head(5))
print(df_unido['MANAGER_ID_x'].head(5))
print(df_unido['MANAGER_ID_y'].head(5))

# 24. Identifique la diferencia en el how con el tipo de join: left, right y outer

# outer

df_outer = pd.merge(df_emp, df_dep, how='outer', on='MANAGER_ID')

print(df_outer.columns)
print('*' * 50)
# This is usefully when we need to combine both df and get all the matches in either left or right join.

# When rows in both the dataframes do not match, the resulting dataframe
# will have NaN for every column of the dataframe that lacks a matching row.

# right and left:

df_ri_le = pd.merge(df_emp, df_dep, left_on='DEPARTMENT_ID', right_on='MANAGER_ID')
print(df_ri_le.columns)
print('*' * 50)

# But, what if the column names are different in the two dataframes?
# Then, we have to explicitly mention both the column names.
#
# ‘left_on’ and ‘right_on’ are two arguments through which we can achieve this.
# ‘left_on’ is the name of the key in the left dataframe and ‘right_on’ in the right dataframe:

print("Nuevo dataframe")
# load employees_43
df_emp = pd.read_csv('./employees_43.csv', sep='-', encoding='UTF-8')

# 24. obersevar la estructura
print(df_emp.columns)
print(df_emp.head(5))
for i in range(len(df_emp.columns)):
    print([df_emp.columns[i]])
print('*' * 50)

# 25. Identifique para cada una de las series los valores nulos.

for i in range(len(df_emp.columns)):
    print(df_emp[df_emp[df_emp.columns[i]].isnull()][[df_emp.columns[i]]])
print('*' * 50)

# 26. Elimine todas las filas que tienen valores nulos.

df_emp.dropna(inplace=True)

# 27. Homogenizar cada serie al tipo de dato que corresponda a la mayoria de sus valores (por ejmplo salary
# según los datos debe ser entero).

# start date as datetime
df_emp['Start Date'] = pd.to_datetime(df_emp['Start Date'])

# salary as int
df_emp['Salary'] = df_emp[df_emp.Salary.str.contains('^[0-9]+$', regex=True)]['Salary']
df_emp['Salary'] = df_emp['Salary'].fillna(0).astype(int)

# Bonus % as float
df_emp['Bonus %'] = df_emp['Bonus %'].str.replace(',', '.')
df_emp['Bonus %'] = df_emp['Bonus %'].fillna(0).astype(float)

# 28. Ordene el DataFrame alfabeticamente por apellido
df_emp.sort_values(by='First Name', inplace=True)

# 29. Asignar una nueva serie que corresponde a la llave, que debe iniciar en 100.

keys_df = pd.Series(np.arange(100, df_emp.shape[0] + 1))
df_emp['Keys'] = keys_df.apply(int)
print(df_emp['Keys'])
print('*' * 50)

# 30. Crear un nuevo DataFrame con los valores únicos de la serie Team.

teams = df_emp['Team'].unique()
team_df = pd.DataFrame(data=teams)
team_df.rename(columns={0: 'Team'}, inplace=True)

# 31. Crearle al anterior DataFrame la llave primaria con un valor enumerado que inicie en 1.

team_key = pd.Series(np.arange(1, team_df.shape[0] + 1))
team_df['Codigo_Team'] = team_key

# 32. Crear una nueva serie con el nombre Codigo_Team en la DataFrame empleados, donde los valores
# numéricos correspondan a la llave del dataframe Team.

df_emp = pd.merge(df_emp, team_df, on='Team')
print(df_emp[df_emp['Team'] == 'Legal'][['Team', 'First Name', 'Codigo_Team']])
print('*' * 50)

# 33. Eliminar la serie Team del DataFrame empleados que contenia los nombres de equipos.

df_emp.drop(['Team'], axis=1, inplace=True)
print(df_emp.columns)
print('*' * 50)

# 34. Cantidad de empleados por equipo (team). Utilice la función groupby()

query = df_emp.groupby('Codigo_Team')
print(query[['First Name']].count())
print('*' * 50)

# 35. Calcular el valor total de los salarios por equipo.

query = df_emp.groupby('Codigo_Team')
print(query[['Salary']].sum())
print('*' * 50)

# 36. Cantidad de mujeres y hombres el dataframe.

query = df_emp.groupby('Gender')
print(query[['First Name']].count())
print('*' * 50)

# 37. Empleados quienes hicieron login en el mes equivalente al mes actual.

print(df_emp[pd.DatetimeIndex(df_emp['Start Date']).month == 12][['Start Date', 'First Name', 'Last Login Time']])
print('*' * 50)

# 38. Cantidad de empleados que hicieron login por año.

query = df_emp.groupby(pd.DatetimeIndex(df_emp['Start Date']).year)
print(query['First Name'].count())
print('*' * 50)

# 39. Cantidad de empleados que no han hecho login en los ultimos quince años.

df_emp_aux = df_emp
df_emp_aux['Start Date'] = df_emp_aux[(pd.DatetimeIndex(df_emp['Start Date']).year < 2007)][['Start Date']]
query = df_emp_aux.groupby(pd.DatetimeIndex(df_emp_aux['Start Date']).year)
print(query['First Name'].count())
print('*' * 50)


