import pandas as pd
from app.logger import get_logger

logger = get_logger(__name__)

def validate_employees(df: pd.DataFrame) -> pd.DataFrame:
    logger.info(f"Validating {len(df)} rows...")

    # Check 1 — Missing emails
    missing_email = df[df["email"].isna() | (df["email"] == "")]
    if not missing_email.empty:
        logger.warning(f"{len(missing_email)} rows with missing email: {list(missing_email['name'])}")

    # Check 2 — Negative salary
    negative_salary = df[df["salary"] < 0]
    if not negative_salary.empty:
        logger.warning(f"{len(negative_salary)} rows with invalid salary: {list(negative_salary['name'])}")

    # Check 3 — Missing joining date
    missing_date = df[df["joining_date"].isna() | (df["joining_date"] == "")]
    if not missing_date.empty:
        logger.warning(f"{len(missing_date)} rows with missing joining date: {list(missing_date['name'])}")

    if missing_email.empty and negative_salary.empty and missing_date.empty:
        logger.info("All rows passed validation!")

    # Clean — remove invalid rows
    df = df[df["email"].notna() & (df["email"] != "")]
    df = df[df["salary"] >= 0]
    df = df[df["joining_date"].notna() & (df["joining_date"] != "")]

    logger.info(f"{len(df)} clean rows ready to load")
    return df

if __name__ == "__main__":
    from app.ingestion.csv_ingestor import fetch_csv
    df = fetch_csv("data/employees.csv")
    clean_df = validate_employees(df)
    logger.info(f"Clean data:\n{clean_df}")