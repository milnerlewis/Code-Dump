import pandas as pd

# Create data array
data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Minnie', 'Donald', 'Daisy', 'Goofy', 'Pluto'],
        'Age': [10, 20, 30, 40],
        'City': ['Sheffield', 'London', 'Manchester', 'Birmingham', 'Sheffield', 'London', 'Manchester', 'Sheffield']}

# Create DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print(df)

# Select rows
for i in range(0, len(df)):
    print(f"Row {i}: {df.loc[i]}")