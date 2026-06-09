import pandas as pd
from sqlalchemy import text
from app.database import engine

def load_users(df: pd.DataFrame):
    # Clear existing data first (for clean re-runs)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE users RESTART IDENTITY CASCADE"))
        conn.commit()

    df.to_sql("users", engine, if_exists="append", index=False)
    print(f"✅ Loaded {len(df)} users into PostgreSQL")

def load_posts(df: pd.DataFrame):
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE posts RESTART IDENTITY CASCADE"))
        conn.commit()

    df.to_sql("posts", engine, if_exists="append", index=False)
    print(f"✅ Loaded {len(df)} posts into PostgreSQL")

if __name__ == "__main__":
    from app.ingestion.api_ingestor import fetch_users, fetch_posts
    from app.transformation.transformer import transform_users, transform_posts

    load_users(transform_users(fetch_users()))
    load_posts(transform_posts(fetch_posts()))