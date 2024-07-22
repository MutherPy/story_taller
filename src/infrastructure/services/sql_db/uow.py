
from infrastructure.persistance.bases.uow import BaseCommonUOW
from infrastructure.services.sql_db.repositories.auth_repository.query import UserQueryRepository
from infrastructure.services.sql_db.repositories.auth_repository.command import UserCommandRepository
from typing import Annotated


class DbUOW(BaseCommonUOW):

    user_q_rep: Annotated[UserQueryRepository, None]
    user_c_rep: Annotated[UserCommandRepository, None]

    async def commit(self):
        await self.dl_connector.commit()

    async def rollback(self):
        await self.dl_connector.rollback()
