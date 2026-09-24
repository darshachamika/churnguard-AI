import pandas as pd


file_path = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"

df = pd.read_csv(file_path)

print("===== DATASET INVESTIGATION =====")


print("\nDataset Shape:")
print(df.shape)


print("\nData Types:")
print(df.dtypes)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nChurn Distribution:")
print(df["Churn"].value_counts())


print("\nNumerical Statistics:")
print(df.describe())


print("\nTotalCharges empty values:")
print((df["TotalCharges"].str.strip() == "").sum())

print("\nRows with empty TotalCharges:")
print(
    df[
        df["TotalCharges"].str.strip() == ""
    ][["customerID", "tenure", "TotalCharges", "Churn"]]
)