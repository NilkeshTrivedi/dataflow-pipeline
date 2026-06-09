from app.database import engine, Base
import app.models  # noqa: F401 - import so models are registered

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully!")

if __name__ == "__main__":
    create_tables()