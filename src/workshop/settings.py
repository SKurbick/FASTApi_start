from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    # database_url: str = "sqlite:///./test.db"
    # database_url: str = "postgresql://user:password@postgresserver/db"
    database_url: str = "postgresql://postgres:6336@localhost:5432/fastapi"

settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
