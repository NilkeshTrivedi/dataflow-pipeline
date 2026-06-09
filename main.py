from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="DataFlow Pipeline API",
    description="ETL Pipeline exposing users, posts, and employee data",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")

@app.get("/", tags=["Health"])
def root():
    return {
        "status": "running",
        "message": "DataFlow Pipeline API is live!",
        "docs": "/docs"
    }

@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy"}