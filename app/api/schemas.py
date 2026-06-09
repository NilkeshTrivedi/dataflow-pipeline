from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None

    class Config:
        from_attributes = True

class PostResponse(BaseModel):
    id: int
    user_id: int
    title: str
    body: Optional[str] = None

    class Config:
        from_attributes = True

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    joining_date: Optional[str] = None

    class Config:
        from_attributes = True

class StatsResponse(BaseModel):
    total_users: int
    total_posts: int
    total_employees: int
    avg_salary: float
    departments: dict