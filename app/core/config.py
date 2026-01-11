from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Playlist Sync Tool")
    ENV = os.getenv("ENV", "development")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
