import pandas as pd

df_emp = pd.read_csv('./employees.csv', sep=';', encoding='UTF-8', on_bad_lines='error')

# exercise 1 - COMMISSION PCT to numeric and reformat - ',' for '.'
df_emp['COMMISSION_PCT'] = df_emp['COMMISSION_PCT'].replace(',', '.')
# Aca se convierte a numerico
df_emp['COMMISSION_PCT'] = pd.to_numeric(df_emp['COMMISSION_PCT'])
# A todos se les asigna el valor de 0
df_emp['COMMISSION_PCT'] = df_emp['COMMISSION_PCT'].fillna(0)

print(df_emp['COMMISSION_PCT'])

print('*' * 50)

# 2. Crear una nueva serie en el DataFrame empleados que calcule el salario por la comisión
newSalary = df_emp['COMMISSION_PCT'] * df_emp['SALARY']
df_emp['NEW_SALARY'] = newSalary

print(df_emp[(df_emp.NEW_SALARY > 0)][['NEW_SALARY', 'FIRST_NAME']])

print('*' * 50)

# 3. Genere un nuevo DataFrame que muestre apellido, salario, fecha de contratación y comisión para los
# empleados que hayan sido contratados en el segundo semestre del 2018 y que la comisión sea superior al
# 25%.

df_emp['HIRE_DATE'] = pd.to_datetime(df_emp['HIRE_DATE'], format='%d/%m/%Y')

query = df_emp[(df_emp.COMMISSION_PCT > 0.25) & (pd.DatetimeIndex(df_emp.HIRE_DATE).year == 2018) & (pd.DatetimeIndex(df_emp.HIRE_DATE).month >= 6)][
    ['FIRST_NAME', 'LAST_NAME', 'SALARY', 'HIRE_DATE', 'COMMISSION_PCT']]

print(query)