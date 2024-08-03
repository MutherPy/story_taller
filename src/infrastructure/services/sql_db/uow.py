
from infrastructure.persistance.bases.uow import BaseCommonUOW
from infrastructure.services.sql_db.repositories.story_repository.command import StoryCommandRepository
from infrastructure.services.sql_db.repositories.story_repository.query import StoryQueryRepository
from infrastructure.services.sql_db.repositories.user_repository.query import UserQueryRepository
from infrastructure.services.sql_db.repositories.user_repository.command import UserCommandRepository
from infrastructure.services.sql_db.repositories.tags_repository.query import TagsQueryRepository
from infrastructure.services.sql_db.repositories.tags_repository.command import TagsCommandRepository

from typing import Annotated


class DbUOW(BaseCommonUOW):

    # TODO change repo creation like just annotation
    user_q_rep: Annotated[UserQueryRepository, None]
    user_c_rep: Annotated[UserCommandRepository, None]

    tags_q_rep: Annotated[TagsQueryRepository, None]
    tags_c_rep: Annotated[TagsCommandRepository, None]

    story_q_rep: Annotated[StoryQueryRepository, None]
    story_c_rep: Annotated[StoryCommandRepository, None]

    async def commit(self):
        await self.dl_connector.commit()

    async def rollback(self):
        await self.dl_connector.rollback()
