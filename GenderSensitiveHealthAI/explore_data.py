import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('disease_data.csv')

# Display the first few rows of the dataset
print(df.head())

# Get the number of rows and columns in the dataset
num_rows, num_cols = df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

# Get summary statistics for numerical columns
print(df.describe())

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Get unique values and their counts for categorical columns
print("Unique diseases:", df['Disease'].nunique())
print("Unique symptoms:", df['Symptoms'].nunique())
print("Unique treatments:", df['Treatments'].nunique())

# Filter out non-numeric columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Correlation Analysis
correlation_matrix = numeric_df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Visualization
# Pairplot for numerical columns
sns.pairplot(numeric_df)
plt.title("Pairplot of Numerical Columns")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
