from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from providers.plugs.infrastructure_common_plugs import sql_db_provider

from infrastructure.services.sql_db.provider import db_proxy_for_provider
from infrastructure.services.sql_db.uow import DbUOW


# sql_db_provider
async def get_sql_db_provider() -> AsyncSession:
    async with db_proxy_for_provider.session() as session:
        yield session


# sql_db_uow_provider
async def get_sql_db_uow_provider(session=Depends(sql_db_provider)):
    return DbUOW(dl_connector=session)

