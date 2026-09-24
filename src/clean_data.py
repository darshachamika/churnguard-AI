import pandas as pd


file_path = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"

df = pd.read_csv(file_path)

print("===== DATA CLEANING =====")

df["TotalCharges"] = df["TotalCharges"].str.strip()
df["TotalCharges"] = df["TotalCharges"].replace("", pd.NA)

print("\nMissing TotalCharges after detecting blanks:")
print(df["TotalCharges"].isnull().sum())


df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)


df["TotalCharges"] = df["TotalCharges"].fillna(0)

print("\nTotalCharges data type:")
print(df["TotalCharges"].dtype)


print("\nRemaining missing TotalCharges:")
print(df["TotalCharges"].isnull().sum())


print("\nCleaned zero-tenure customers:")
print(
    df[df["tenure"] == 0][
        ["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]
    ]
)


print("\nDataset shape after cleaning:")
print(df.shape)


print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())