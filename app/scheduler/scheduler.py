from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
from app.ingestion.api_ingestor import fetch_users, fetch_posts
from app.ingestion.csv_ingestor import fetch_csv
from app.transformation.transformer import transform_users, transform_posts
from app.validation.validator import validate_employees
from app.loader.loader import load_users, load_posts, load_employees
from app.logger import get_logger

logger = get_logger(__name__)

def run_pipeline():
    logger.info(f"Pipeline started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        # Step 1 - Ingest
        raw_users = fetch_users()
        raw_posts = fetch_posts()
        raw_employees = fetch_csv("data/employees.csv")

        # Step 2 - Transform & Validate
        clean_users = transform_users(raw_users)
        clean_posts = transform_posts(raw_posts)
        clean_employees = validate_employees(raw_employees)

        # Step 3 - Load
        load_users(clean_users)
        load_posts(clean_posts)
        load_employees(clean_employees)

        logger.info(f"Pipeline completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=run_pipeline,
        trigger=IntervalTrigger(hours=1),
        id="etl_pipeline",
        name="ETL Pipeline",
        replace_existing=True
    )
    scheduler.start()
    logger.info("Scheduler started — pipeline runs every 1 hour")
    return scheduler