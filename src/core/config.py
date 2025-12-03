from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    BASE_URL: str
    TECHNICAL_MODEL: str
    TEXTUAL_MODEL: str
    FILE: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
