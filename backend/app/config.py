from pydantic_settings import BaseSettings  

class Settings(BaseSettings):
    app_name: str = "FastAPI Shop"
    debug: bool = True
    database_url: str = "sqlite:/// ./shop.db"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3800",
        "http://127.0.0.1:5173",
        "http://localhost:3800"
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file = "venv"

settings = Settings()