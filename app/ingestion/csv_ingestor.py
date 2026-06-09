import pandas as pd
import os

def fetch_csv(filepath: str) -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")

    df = pd.read_csv(filepath)
    print(f"✅ Loaded {len(df)} rows from {filepath}")
    print(f"   Columns: {list(df.columns)}")
    return df

if __name__ == "__main__":
    df = fetch_csv("data/employees.csv")
    print(df)