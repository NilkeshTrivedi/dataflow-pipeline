import pandas as pd
from app.transformation.transformer import transform_users, transform_posts

# Sample raw API data (same structure as JSONPlaceholder)
SAMPLE_USERS = [
    {
        "id": 1,
        "name": "  Nilkesh Trivedi  ",
        "username": "nilkesh",
        "email": "NILKESH@TEST.COM",
        "phone": "1234567890",
        "website": "nilkesh.dev",
        "address": {"city": "Vadodara"},
        "company": {"name": "Accenture"}
    },
    {
        "id": 2,
        "name": "Priya Patel",
        "username": "priya",
        "email": "priya@test.com",
        "phone": "9876543210",
        "website": "priya.dev",
        "address": {"city": "Mumbai"},
        "company": {"name": "TCS"}
    }
]

SAMPLE_POSTS = [
    {"userId": 1, "id": 1, "title": "  hello world  ", "body": "test body"},
    {"userId": 1, "id": 2, "title": "second post", "body": "another body"},
]

def test_transform_users_returns_dataframe():
    df = transform_users(SAMPLE_USERS)
    assert isinstance(df, pd.DataFrame)

def test_transform_users_correct_columns():
    df = transform_users(SAMPLE_USERS)
    expected = ["id", "name", "username", "email", "phone", "website", "city", "company"]
    assert list(df.columns) == expected

def test_transform_users_email_lowercase():
    df = transform_users(SAMPLE_USERS)
    assert df["email"].iloc[0] == "nilkesh@test.com"

def test_transform_users_name_stripped():
    df = transform_users(SAMPLE_USERS)
    assert df["name"].iloc[0] == "Nilkesh Trivedi"

def test_transform_users_extracts_city():
    df = transform_users(SAMPLE_USERS)
    assert df["city"].iloc[0] == "Vadodara"

def test_transform_users_extracts_company():
    df = transform_users(SAMPLE_USERS)
    assert df["company"].iloc[0] == "Accenture"

def test_transform_users_count():
    df = transform_users(SAMPLE_USERS)
    assert len(df) == 2

def test_transform_posts_returns_dataframe():
    df = transform_posts(SAMPLE_POSTS)
    assert isinstance(df, pd.DataFrame)

def test_transform_posts_renames_userid():
    df = transform_posts(SAMPLE_POSTS)
    assert "user_id" in df.columns
    assert "userId" not in df.columns

def test_transform_posts_title_capitalized():
    df = transform_posts(SAMPLE_POSTS)
    assert df["title"].iloc[0] == "Hello world"