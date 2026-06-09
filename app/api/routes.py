from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, text
from app.database import get_db
from app.models import User, Post, Employee
from app.api.schemas import UserResponse, PostResponse, EmployeeResponse, StatsResponse
from typing import Optional

router = APIRouter()

# ── Users ──────────────────────────────────────────

@router.get("/users", response_model=list[UserResponse], tags=["Users"])
def get_users(
    city: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(User)
    if city:
        query = query.filter(User.city.ilike(f"%{city}%"))
    users = query.all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

@router.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user

# ── Posts ──────────────────────────────────────────

@router.get("/posts", response_model=list[PostResponse], tags=["Posts"])
def get_posts(
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Post)
    if user_id:
        query = query.filter(Post.user_id == user_id)
    posts = query.all()
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")
    return posts

@router.get("/posts/{post_id}", response_model=PostResponse, tags=["Posts"])
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post {post_id} not found")
    return post

# ── Employees ──────────────────────────────────────

@router.get("/employees", response_model=list[EmployeeResponse], tags=["Employees"])
def get_employees(
    department: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Employee)
    if department:
        query = query.filter(Employee.department.ilike(f"%{department}%"))
    employees = query.all()
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found")
    return employees

# ── Stats ──────────────────────────────────────────

@router.get("/stats", response_model=StatsResponse, tags=["Analytics"])
def get_stats(db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    total_posts = db.query(Post).count()
    total_employees = db.query(Employee).count()

    avg_salary = db.query(func.avg(Employee.salary)).scalar() or 0

    dept_rows = db.query(
        Employee.department,
        func.count(Employee.id)
    ).group_by(Employee.department).all()

    departments = {dept: count for dept, count in dept_rows}

    return StatsResponse(
        total_users=total_users,
        total_posts=total_posts,
        total_employees=total_employees,
        avg_salary=round(avg_salary, 2),
        departments=departments
    )

from datetime import datetime

pipeline_log = []

@router.get("/pipeline/status", tags=["Pipeline"])
def pipeline_status():
    return {
        "status": "running",
        "last_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "schedule": "Every 1 hour",
        "endpoints": {
            "users": "/api/v1/users",
            "posts": "/api/v1/posts",
            "employees": "/api/v1/employees",
            "stats": "/api/v1/stats"
        }
    }

