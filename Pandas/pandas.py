import pandas as pd

dataFile = pd.read_csv('sheffielddatacsv.csv')

print(dataFile.to_string())
