from pydantic_settings import BaseSettings
from pydantic import Field


class SQLDBSettings(BaseSettings):
    USER: str = Field(default='user', alias='POSTGRES_USER')
    PASSWORD: str = Field(default='password', alias='POSTGRES_PASSWORD')
    DB: str = Field(default='db', alias='POSTGRES_DB')
    HOST: str = 'localhost'
    PORT: int = 5432
    DISABLE_POOL: bool = True

    DRIVER: str = 'postgresql+asyncpg'
    DRIVER_SYNC: str = 'postgresql+psycopg2'

    @property
    def db_url(self):
        return (
            f'{self.DRIVER}://{self.USER}:{self.PASSWORD}@'
            f'{self.HOST}:{self.PORT}/{self.DB}'
        )

    @property
    def db_url_sync(self):
        return (
            f'{self.DRIVER_SYNC}://{self.USER}:{self.PASSWORD}@'
            f'{self.HOST}:{self.PORT}/{self.DB}'
        )
