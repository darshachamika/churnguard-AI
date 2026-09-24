import pandas as pd

# Load dataset
file_path = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"

df = pd.read_csv(file_path)

print("===== DATASET INVESTIGATION =====")

# 1. Shape
print("\nDataset Shape:")
print(df.shape)

# 2. Data types
print("\nData Types:")
print(df.dtypes)

# 3. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 5. Unique values in Churn
print("\nChurn Distribution:")
print(df["Churn"].value_counts())

# 6. Numerical statistics
print("\nNumerical Statistics:")
print(df.describe())