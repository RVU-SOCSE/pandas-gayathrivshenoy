import pandas as pd

# Creating a DataFrame using a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Adding a new column with calculated values (e.g., Marks + 5 bonus)
df['Final Marks'] = df['Marks'] + 5

# Display updated DataFrame
print("\nDataFrame after adding new column:")
print(df)
