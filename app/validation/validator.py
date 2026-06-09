import pandas as pd

def validate_employees(df: pd.DataFrame) -> pd.DataFrame:
    print(f"\n🔍 Validating {len(df)} rows...")
    issues = []

    # Check 1 — Missing emails
    missing_email = df[df["email"].isna() | (df["email"] == "")]
    if not missing_email.empty:
        issues.append(f"⚠️  {len(missing_email)} rows with missing email: {list(missing_email['name'])}")

    # Check 2 — Negative salary
    negative_salary = df[df["salary"] < 0]
    if not negative_salary.empty:
        issues.append(f"⚠️  {len(negative_salary)} rows with invalid salary: {list(negative_salary['name'])}")

    # Check 3 — Missing joining date
    missing_date = df[df["joining_date"].isna() | (df["joining_date"] == "")]
    if not missing_date.empty:
        issues.append(f"⚠️  {len(missing_date)} rows with missing joining date: {list(missing_date['name'])}")

    # Print all issues
    if issues:
        print("Validation Issues Found:")
        for issue in issues:
            print(" ", issue)
    else:
        print("✅ All rows passed validation!")

    # Clean — remove invalid rows
    df = df[df["email"].notna() & (df["email"] != "")]
    df = df[df["salary"] >= 0]
    df = df[df["joining_date"].notna() & (df["joining_date"] != "")]

    print(f"✅ {len(df)} clean rows ready to load")
    return df

if __name__ == "__main__":
    from app.ingestion.csv_ingestor import fetch_csv
    df = fetch_csv("data/employees.csv")
    clean_df = validate_employees(df)
    print("\nClean data:")
    print(clean_df)