from application.mappers.story_mapper import StoryDBDTOMapper
from infrastructure.persistance.bases.repository import BaseRepository

from infrastructure.services.sql_db.models.content.story import StoryDB
from infrastructure.services.sql_db.models.many_to_many.stories_tags import story_to_tags_association_table

from sqlalchemy import insert


class StoryCommandRepository(BaseRepository):

    story_mapper: StoryDBDTOMapper

    async def create_story(self, author_id, title, text, tags_ids):
        story = StoryDB(
            author_id=author_id,
            title=title,
            text=text
        )
        self.dl_connector.add(story)
        await self.dl_connector.flush()
        for tag_id in tags_ids:
            stmt = insert(story_to_tags_association_table).values(
                tag_id=tag_id,
                story_id=story.id
            )
            await self.dl_connector.execute(stmt)
        return True
