"""Настройки сервера."""
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    """Параметры сервера."""

    host: str = 'localhost'
    port: int = 8080
    reload: bool = False
