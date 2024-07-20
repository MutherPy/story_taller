import contextlib
from typing import AsyncIterator, Optional

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from configs.main_config import Config
from configs.config_loader import LoadedConfig


class AsyncDBProxy:
    def __init__(self, config: Config = LoadedConfig):
        self.config = config
        self.db_engine_async: Optional[AsyncEngine] = None
        self.db_sessionmaker_async: Optional[async_sessionmaker[AsyncSession]] = None
        self.initialized: bool = False

    @classmethod
    def initialize(cls) -> "AsyncDBProxy":
        async_db_proxy = cls()
        async_db_proxy.db_engine_async = async_db_proxy._create_async_engine()
        async_db_proxy.db_sessionmaker_async = async_db_proxy._async_session_factory()
        async_db_proxy.initialized = True
        return async_db_proxy

    def _create_async_engine(self) -> AsyncEngine:
        if self.config.db.DISABLE_POOL:
            return create_async_engine(self.config.db.db_url, poolclass=NullPool)
        return create_async_engine(self.config.db.db_url)

    def _async_session_factory(self) -> async_sessionmaker[AsyncSession]:
        session_factory = async_sessionmaker(bind=self.db_engine_async, autoflush=False, expire_on_commit=False)
        return session_factory

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if not self.initialized:
            raise RuntimeError('AsyncDBProxy not initialized')
        session = self.db_sessionmaker_async()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
