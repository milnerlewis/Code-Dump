import pandas as pd

# Create data array
data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Minnie', 'Donald', 'Daisy', 'Goofy', 'Pluto'],
        'Age': [18, 35, 28, 45, 50, 30, 29, 35],
        'City': ['Sheffield', 'London', 'Manchester', 'Birmingham', 'Sheffield', 'London', 'Manchester', 'Sheffield']}

# Create DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print(df, "\n\n\nRow Select:\n")

# Select rows
selectRow1 = df.loc[0]
selectRow2 = df.loc[1]
selectRow3 = df.loc[2]

print(f"Row 1:\n{selectRow1}\n")
print(f"Row 2:\n{selectRow2}\n")
print(f"Row 3:\n{selectRow3}\n")


# Slice data
selectedColumns = df.loc[:, ['Name', 'City']]
print("\nColumn select:\n", selectedColumns)


# GroupBy - Average age by town:
#print(df.groupby(['City']).mean())
