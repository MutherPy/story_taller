
from infrastructure.persistance.bases.uow import BaseCommonUOW
from infrastructure.services.sql_db.repositories.auth_repository.query import UserQueryRepository
from infrastructure.services.sql_db.repositories.auth_repository.command import UserCommandRepository
from infrastructure.services.sql_db.repositories.tags_repository.query import TagsQueryRepository
from infrastructure.services.sql_db.repositories.tags_repository.command import TagsCommandRepository

from typing import Annotated


class DbUOW(BaseCommonUOW):

    # TODO change repo creation like just annotation
    user_q_rep: Annotated[UserQueryRepository, None]
    user_c_rep: Annotated[UserCommandRepository, None]

    tags_q_rep: Annotated[TagsQueryRepository, None]
    tags_c_rep: Annotated[TagsCommandRepository, None]

    async def commit(self):
        await self.dl_connector.commit()

    async def rollback(self):
        await self.dl_connector.rollback()
