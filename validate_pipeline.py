import pandas as pd
import numpy as np

def run_audit(df):
    print("--- Data Quality Audit Report ---")
    
    # 1. Missing Values
    missing = df.isnull().sum()
    print("\nMissing Values:")
    print(missing[missing > 0])
    
    # 2. Duplicate Rows
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")
    
    # 3. Data Types Check
    print("\nData Types:")
    print(df.dtypes)
    
    # 4. Numerical Outliers (Simple Z-score check)
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
        outliers = (z_scores > 3).sum()
        if outliers > 0:
            print(f"Outliers in {col}: {outliers}")

if __name__ == "__main__":
    try:
        data = pd.read_csv('CLEANED-butcher-sales-dirty-4000-CLEANED VERSION -EN-csv.csv')
        run_audit(data)
    except FileNotFoundError:
        print("Dataset not found.")
