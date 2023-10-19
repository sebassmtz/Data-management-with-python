import pandas as pd

data = pd.read_csv("employees.csv", sep=';')

serie = data[['FIRST_NAME', 'EMPLOYEE_ID']]

print(serie.head())

query1 = data.loc[100:100,['FIRST_NAME', 'EMPLOYEE_ID']]
query2 = data.iloc[7:8]
print(query2)