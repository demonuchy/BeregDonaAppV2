from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import  ConfigDict


class Settings(BaseSettings):
    """Настройкт проекта"""

    DB_USER : str
    DB_PASS : str
    DB_HOST : str
    DB_NAME : str
    DB_PORT : int
    DB_CONTAINER_NAME : str

    REDIS_HOST : str
    REDIS_PORT : str
    REDIS_CONTAINER_NAME : str

    JWT_SECRET_KEY : str
    JWT_ACCESS_EXPIRE_MINETS : int
    JWT_REFRESH_EXPIRE_MINETS : int
    JWT_ALGORITM : str
    JWT_KID : str

    TOKEN_BOT : str
    WEBHOOK_TUNNEL_URL : str
    WEBHOOK_SECRET_KEY : str

    @property
    def AsyncDataBaseUrl(self):
        """Url для подключения к базе данных"""
        uri = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_CONTAINER_NAME}:{self.DB_PORT}/{self.DB_NAME}"
        return uri

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
        env_nested_delimiter="__"
    )

config = Settings()