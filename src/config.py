from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from . import utils


@utils.Singleton
class Settings(BaseSettings):
    APP_TITLE: str = "UDV Summer Camp Test"
    APP_DESCRIPTION: str = "API for UDV Summer Camp Test"
    APP_VERSION: str = "0.1.0"

    DEBUG: bool = False

    CSRF_COOKIE_NAME: str = "csrftoken"
    CSRF_EXPIRE_TIME: int = 86400 * 7  # 7 дней

    DOMAIN: str = "example.site"

    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_HOSTS: list[str] = ["*"]

    API_PREFIX: str = "/api"

    model_config = SettingsConfigDict(env_file=Path(__file__).parents[1] / ".env", extra="ignore")


def get_settings():
    return Settings()
