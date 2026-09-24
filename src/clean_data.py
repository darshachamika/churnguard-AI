
from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
CLEAN_PATH = BASE_DIR / "data" / "processed" / "telco_churn_clean.csv"


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and validate the Telco Customer Churn dataset."""

    
    df = df.copy()

    
    duplicate_ids = df["customerID"].duplicated().sum()

    if duplicate_ids > 0:
        raise ValueError(
            f"Found {duplicate_ids} duplicate customer IDs."
        )

    
    charges = df["TotalCharges"].astype("string").str.strip()
    blank_mask = charges.isna() | charges.eq("").fillna(False)

    print(f"Blank TotalCharges: {blank_mask.sum()}")

    
    unexpected_blanks = blank_mask & df["tenure"].ne(0)

    if unexpected_blanks.any():
        raise ValueError(
            "Found blank TotalCharges for customers with tenure > 0."
        )

    
    df["TotalCharges"] = pd.to_numeric(
        charges.mask(blank_mask),
        errors="raise"
    )

    
    df.loc[blank_mask, "TotalCharges"] = 0.0

    
    if df["TotalCharges"].isna().any():
        raise ValueError("TotalCharges still contains missing values.")

    if df.isna().any().any():
        raise ValueError("Dataset contains missing values.")

    if df["customerID"].duplicated().any():
        raise ValueError("Duplicate customer IDs detected.")

    return df


def main():
    print("===== CHURNGUARD DATA CLEANING =====")

    df = pd.read_csv(RAW_PATH)
    original_shape = df.shape

    cleaned_df = clean_customer_data(df)

    assert cleaned_df.shape == original_shape, (
        "Dataset shape changed unexpectedly."
    )

    
    CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(CLEAN_PATH, index=False)

    print("\nCleaned dataset shape:", cleaned_df.shape)
    print("TotalCharges dtype:", cleaned_df["TotalCharges"].dtype)
    print("Missing values:", cleaned_df.isna().sum().sum())
    print("Duplicate customer IDs:",
          cleaned_df["customerID"].duplicated().sum())
    print("Saved to:", CLEAN_PATH)


if __name__ == "__main__":
    main()