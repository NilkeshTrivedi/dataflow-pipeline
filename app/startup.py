from app.database import engine, Base
import app.models
from app.loader.loader import load_users, load_posts, load_employees
from app.ingestion.api_ingestor import fetch_users, fetch_posts
from app.ingestion.csv_ingestor import fetch_csv
from app.transformation.transformer import transform_users, transform_posts
from app.validation.validator import validate_employees
from app.logger import get_logger

logger = get_logger(__name__)

def initialize():
    logger.info("Creating tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Tables ready")

    logger.info("Running initial pipeline...")
    try:
        load_users(transform_users(fetch_users()))
        load_posts(transform_posts(fetch_posts()))
        load_employees(validate_employees(fetch_csv("data/employees.csv")))
        logger.info("Initial data loaded successfully")
    except Exception as e:
        logger.warning(f"Initial load warning: {e}")