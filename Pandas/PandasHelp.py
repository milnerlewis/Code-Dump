import pandas as pd

# Create data array
data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Minnie', 'Donald', 'Daisy', 'Goofy', 'Pluto'],
        'Age': [18, 35, 28, 45, 50, 30, 29, 35],
        'City': ['Sheffield', 'London', 'Manchester', 'Birmingham', 'Sheffield', 'London', 'Manchester', 'Sheffield']}

# Create DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print(df)

# Select rows
print(f"Row 1: {df.loc[0]}")
print(f"Row 2: {df.loc[1]}")
print(f"Row 3: {df.loc[2]}")
