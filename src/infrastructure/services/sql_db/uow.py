
from infrastructure.persistance.bases.uow import BaseCommonUOW
from infrastructure.services.sql_db.repositories.auth_repository.query import UserQueryRepository
from infrastructure.services.sql_db.repositories.auth_repository.command import UserCommandRepository
from typing import Annotated
from interfaces.infrastructure.uows.sql_db import IDBUoW


class DbUOW(BaseCommonUOW, IDBUoW):

    # TODO change repo creation like just annotation
    user_q_rep: Annotated[UserQueryRepository, None]
    user_c_rep: Annotated[UserCommandRepository, None]

    async def commit(self):
        await self.dl_connector.commit()

    async def rollback(self):
        await self.dl_connector.rollback()
