from fastapi import Depends

from infrastructure.persistance.main_uow import MainUOW
from providers.plugs.infrastructure_common_plugs import sql_db_uow_provider


# main_uow_provider
async def get_main_uow_provider(db=Depends(sql_db_uow_provider)):
    return MainUOW(db=db)
