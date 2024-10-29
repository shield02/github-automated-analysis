# app/config.py
from pydantic import BaseSettings

class Config(BaseSettings):
    github_api_token: str
    openai_api_key: str

    class Config:
        env_file = "../.env"

config = Config()
