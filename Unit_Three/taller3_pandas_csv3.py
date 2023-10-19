import pandas as pd
import os

from pathlib import Path

retval = os.getcwd()
print(retval)

current_directory = Path.cwd()
print("Directorio actual:", current_directory)

# Now change the directory
os.chdir(current_directory)

data = pd.read_csv('employees.csv', sep=';')


#import from json file

import json 
with open('_personFile.json','r') as j:
    data = json.load(j)

dataframe = pd.DataFrame(data)

dataframe.to_csv('filepersonas.csv', index=False)