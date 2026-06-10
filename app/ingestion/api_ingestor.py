import requests
from app.config import settings
from app.logger import get_logger

logger = get_logger(__name__)

def fetch_users() -> list[dict]:
    url = f"{settings.API_URL}/users"
    response = requests.get(url)
    response.raise_for_status()
    users = response.json()
    logger.info(f"Fetched {len(users)} users from API")
    return users

def fetch_posts() -> list[dict]:
    url = f"{settings.API_URL}/posts"
    response = requests.get(url)
    response.raise_for_status()
    posts = response.json()
    logger.info(f"Fetched {len(posts)} posts from API")
    return posts

if __name__ == "__main__":
    users = fetch_users()
    posts = fetch_posts()
    logger.info(f"Sample user: {users[0]}")
    logger.info(f"Sample post: {posts[0]}")