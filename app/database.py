from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("Connected to PostgreSQL:", result.fetchone()[0])

if __name__ == "__main__":
    test_connection()