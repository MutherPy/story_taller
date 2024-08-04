from application.mappers.stories_mapper import StoryDBDTOMapper
from infrastructure.persistance.bases.repository import BaseRepository
from infrastructure.services.sql_db.models import TagDB, story_to_tags_association_table

from infrastructure.services.sql_db.models.content.story import StoryDB
from sqlalchemy import select
from application.dto.stories.stories import StoryDTOList, StoryDTORetrieve
from infrastructure.services.sql_db.models.many_to_many.users_tags import users_to_tags_association_table
from infrastructure.services.sql_db.models.users.user import UserDB


class StoryQueryRepository(BaseRepository):

    story_mapper: StoryDBDTOMapper

    async def get_user_stories(self, user_id, tags_ids) -> list[StoryDTOList]:

        tags_filtering = tags_ids.db_filter_int_in(TagDB, rename={'tags_ids': 'id'})

        stmt = select(StoryDB).join(story_to_tags_association_table).join(TagDB).join_from(
            story_to_tags_association_table,
            users_to_tags_association_table,
            story_to_tags_association_table.c.tag_id == users_to_tags_association_table.c.tag_id
        ).where(
            users_to_tags_association_table.c.user_id == user_id,
        ).where(
            *tags_filtering
        ).distinct()
        result = (await self.dl_connector.scalars(stmt))
        return self.story_mapper.list__story_db__to__story_dto_list(result)

    async def get_story_by_id(self, story_id) -> StoryDTORetrieve:
        stmt = select(StoryDB).where(StoryDB.id == story_id)
        result = (await self.dl_connector.scalar(stmt))
        return self.story_mapper.story_db__to__story_dto_retrieve(result)

    async def get_stories_by_tags_ids(self, tags_ids) -> list[StoryDTOList]:
        stmt = select(StoryDB).join(StoryDB.tags).where(TagDB.id.in_(tags_ids))
        result = (await self.dl_connector.scalars(stmt))
        return self.story_mapper.list__story_db__to__story_dto_list(result)
