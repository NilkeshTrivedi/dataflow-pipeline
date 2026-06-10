from app.database import engine, Base
import app.models
from app.loader.loader import load_users, load_posts, load_employees
from app.ingestion.api_ingestor import fetch_users, fetch_posts
from app.ingestion.csv_ingestor import fetch_csv
from app.transformation.transformer import transform_users, transform_posts
from app.validation.validator import validate_employees
import time

def initialize():
    print("⏳ Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables ready")

    print("⏳ Running initial pipeline...")
    try:
        load_users(transform_users(fetch_users()))
        load_posts(transform_posts(fetch_posts()))
        load_employees(validate_employees(fetch_csv("data/employees.csv")))
        print("✅ Initial data loaded")
    except Exception as e:
        print(f"⚠️ Initial load warning: {e}")