from application.mappers.stories_mapper import StoryDBDTOMapper
from infrastructure.persistance.bases.repository import BaseRepository
from infrastructure.services.sql_db.models import TagDB

from infrastructure.services.sql_db.models.content.story import StoryDB
from sqlalchemy import select
from application.dto.stories.stories import StoryDTOList, StoryDTORetrieve
from infrastructure.services.sql_db.models.users.user import UserDB


class StoryQueryRepository(BaseRepository):

    story_mapper: StoryDBDTOMapper

    async def get_user_stories(self, user_id) -> list[StoryDTOList]:
        user_stmt = select(UserDB).where(UserDB.id == user_id)
        result = (await self.dl_connector.scalar(user_stmt))
        stms = select(StoryDB).join(StoryDB.tags).where(
            TagDB.id.in_(
                [i.id for i in result.tags]
            )
        ).distinct()
        result = (await self.dl_connector.scalars(stms))
        return self.story_mapper.list__story_db__to__story_dto_list(result)

    async def get_story_by_id(self, story_id) -> StoryDTORetrieve:
        stmt = select(StoryDB).where(StoryDB.id == story_id)
        result = (await self.dl_connector.scalar(stmt))
        return self.story_mapper.story_db__to__story_dto_retrieve(result)

    async def get_stories_by_tags_ids(self, tags_ids) -> list[StoryDTOList]:
        stmt = select(StoryDB).join(StoryDB.tags).where(TagDB.id.in_(tags_ids))
        result = (await self.dl_connector.scalars(stmt))
        return self.story_mapper.list__story_db__to__story_dto_list(result)
