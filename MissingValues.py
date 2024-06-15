import pandas as pd
from sklearn.impute import SimpleImputer

# Load CSV data into a pandas DataFrame
file_path = 'integrated_sensor_data.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Display initial information about missing values
print("Initial missing value counts:")
print(df.isnull().sum())

# Define imputation strategy (mean, median, most_frequent, etc.)
imputer = SimpleImputer(strategy='mean')

# Identify columns with missing values (assuming numerical data)
cols_with_missing = df.columns[df.isnull().any()].tolist()

# Impute missing values
for col in cols_with_missing:
    df[col] = imputer.fit_transform(df[[col]])

df.drop(columns=['Direction (°)'], inplace=True)
# Display final information about missing values after imputation
print("\nMissing value counts after imputation:")
print(df.isnull().sum())

# Optionally, save the DataFrame with imputed values back to CSV
df.to_csv('imputed_data.csv', index=False)
