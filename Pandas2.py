import pandas as pd

# Load CSV file
# Replace with your actual file path
df = pd.read_csv('Mcd.csv')

# Display original data
print("Original Data:")
print(df)

# Identify missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing values with mean (only for numeric columns)
df_filled = df.fillna(df.mean(numeric_only=True))

# Display updated data
print("\nData after filling missing values with mean:")
print(df_filled)
