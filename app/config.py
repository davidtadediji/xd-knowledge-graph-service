# app/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str
    S3_BUCKET: str
    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str
    S3_REGION: str
    S3_ENDPOINT: str
    OPENAI_API_KEY: str

    # Application Settings
    LOG_LEVEL: str

    class ConfigDict:
        env_file = ".env"


settings = Settings()
