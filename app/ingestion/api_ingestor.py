import requests
from app.config import settings

def fetch_users() -> list[dict]:
    url = f"{settings.API_URL}/users"
    response = requests.get(url)
    response.raise_for_status()
    users = response.json()
    print(f"✅ Fetched {len(users)} users from API")
    return users

def fetch_posts() -> list[dict]:
    url = f"{settings.API_URL}/posts"
    response = requests.get(url)
    response.raise_for_status()
    posts = response.json()
    print(f"✅ Fetched {len(posts)} posts from API")
    return posts

if __name__ == "__main__":
    users = fetch_users()
    posts = fetch_posts()
    print("\nSample user:", users[0])
    print("\nSample post:", posts[0])