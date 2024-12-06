import pandas as pd
from matplotlib import pyplot as plt

dataView = "y"
min = 100
max = -100
mm = 100
yyyy = 1800
rowList = []

dataFile = pd.read_csv('sheffielddata.csv', usecols=['YYYY', 'MM', 'T_Min'])

def dataYearSelect(yearNum):
    rowSelect = ((int(yearNum)-1883) * 12) + 1
    return rowSelect

def displayData():
    dataFile = pd.read_csv('sheffielddata.csv', skiprows=rowSelect, nrows=(11))
    return dataFile

for index, row in dataFile.iterrows():
    data = (index, row["YYYY"], row["MM"], row["T_Min"])

print(rowList)
    
    
while "y" in dataView:

    yearNum = input('What year would you like to view data for (1883-2024)? ')

    if (yearNum.isdigit() == True) and (1882 < int(yearNum)) and (int(yearNum) < 2025):
        rowSelect = dataYearSelect(yearNum)

    else:
        print('\nInvalid input, please try again.')
        continue

    if rowSelect == 1693:
        dataFile = pd.read_csv('sheffielddata.csv', skiprows=rowSelect, nrows=8)
    
    print(displayData())

    dataView = input('\n\n\nWould you like to select a new year (y or n)? ')


print('\n\n\nThank you for viewing our data.')
