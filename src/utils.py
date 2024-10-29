# app/utils.py
import httpx
from .config import config

async def fetch_repos(username: str):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {config.github_api_token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
        return response.json()
