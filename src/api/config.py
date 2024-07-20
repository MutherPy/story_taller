from pydantic_settings import BaseSettings


class ApiConfig(BaseSettings):
    APP: str = 'main:app'
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    ASGI_LOG_LEVEL: str = 'debug'
    APP_DEBUG: bool = True
