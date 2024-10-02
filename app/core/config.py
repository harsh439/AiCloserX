import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    PROJECT_NAME: str = "AI Customer Care"
    VERSION: str = "1.0.0"
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    MONGODB_DB_NAME: str = os.getenv("MONGODB_DB_NAME", "customer_care_db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
