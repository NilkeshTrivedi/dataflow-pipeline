import pandas as pd
from app.validation.validator import validate_employees

SAMPLE_DATA = pd.DataFrame([
    {"id": 1, "name": "Nilkesh", "email": "nilkesh@test.com", "department": "Engineering", "salary": 75000, "joining_date": "2023-01-15"},
    {"id": 2, "name": "Priya",   "email": "",                 "department": "HR",          "salary": 55000, "joining_date": "2023-03-20"},
    {"id": 3, "name": "Rahul",   "email": "rahul@test.com",   "department": "Engineering", "salary": -500,  "joining_date": "2023-06-01"},
    {"id": 4, "name": "Sneha",   "email": "sneha@test.com",   "department": "Finance",     "salary": 60000, "joining_date": ""},
    {"id": 5, "name": "Vikram",  "email": "vikram@test.com",  "department": "Engineering", "salary": 90000, "joining_date": "2023-08-25"},
])

def test_validator_removes_missing_email():
    clean = validate_employees(SAMPLE_DATA.copy())
    assert "Priya" not in clean["name"].values

def test_validator_removes_negative_salary():
    clean = validate_employees(SAMPLE_DATA.copy())
    assert "Rahul" not in clean["name"].values

def test_validator_removes_missing_date():
    clean = validate_employees(SAMPLE_DATA.copy())
    assert "Sneha" not in clean["name"].values

def test_validator_keeps_valid_rows():
    clean = validate_employees(SAMPLE_DATA.copy())
    assert "Nilkesh" in clean["name"].values
    assert "Vikram" in clean["name"].values

def test_validator_correct_count():
    clean = validate_employees(SAMPLE_DATA.copy())
    assert len(clean) == 2

def test_validator_returns_dataframe():
    clean = validate_employees(SAMPLE_DATA.copy())
    assert isinstance(clean, pd.DataFrame)