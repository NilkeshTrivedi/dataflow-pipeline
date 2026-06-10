import pandas as pd
from app.logger import get_logger

logger = get_logger(__name__)

def transform_users(raw_users: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(raw_users)

    # Extract nested fields
    df["city"] = df["address"].apply(lambda x: x.get("city", ""))
    df["company"] = df["company"].apply(lambda x: x.get("name", ""))

    # Select only columns we need
    df = df[["id", "name", "username", "email", "phone", "website", "city", "company"]]

    # Clean up
    df["email"] = df["email"].str.lower().str.strip()
    df["phone"] = df["phone"].str.strip()
    df["name"] = df["name"].str.strip()

    # Drop duplicates
    df = df.drop_duplicates(subset=["email"])

    # Drop rows with missing critical fields
    df = df.dropna(subset=["name", "email", "username"])

    logger.info(f"Transformed {len(df)} users")

    return df

def transform_posts(raw_posts: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(raw_posts)

    # Rename columns to match our model
    df = df.rename(columns={"userId": "user_id"})

    # Select only columns we need
    df = df[["id", "user_id", "title", "body"]]

    # Clean up
    df["title"] = df["title"].str.strip().str.capitalize()
    df["body"] = df["body"].str.strip()

    # Drop duplicates and nulls
    df = df.drop_duplicates(subset=["id"])
    df = df.dropna(subset=["title", "body"])

    logger.info(f"Transformed {len(df)} posts")
    return df

if __name__ == "__main__":
    from app.ingestion.api_ingestor import fetch_users, fetch_posts

    users_df = transform_users(fetch_users())
    posts_df = transform_posts(fetch_posts())

    logger.info(f"Users sample:\n{users_df.head(3)}")
    logger.info(f"Posts sample:\n{posts_df.head(3)}")