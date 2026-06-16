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
            print(f"Found {outliers} outliers in {col}")

    # 5. Handling Missing Dates
    if 'Date' in df.columns:
        mask = df['Date'].isna()
        if 'Audit Notes' not in df.columns:
            df['Audit Notes'] = ''
        df.loc[mask, 'Audit Notes'] = df.loc[mask, 'Audit Notes'].apply(
            lambda x: (str(x) + ' | ' if x and str(x).strip() else '') + '🚨 Missing Date - Flagged for Review'
        )

if __name__ == "__main__":
    # Example usage (simplified for simulation)
    data = {
        'Date': ['2023-01-01', None, '2023-01-03'],
        'Sales': [100, 200, 150],
        'Audit Notes': ['', '', '']
    }
    df = pd.DataFrame(data)
    run_audit(df)
    print("\nFinal DataFrame:")
    print(df)
