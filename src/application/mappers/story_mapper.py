from application.bases.base_mapper import BaseMapper

from infrastructure.services.sql_db.models.content.story import StoryDB
from application.dto.stories.stories import StoryDTORetrieve, StoryDTOList

from application.mappers.users_mapper import UserDBDTOMapper


class StoryDBDTOMapper(BaseMapper):

    @staticmethod
    def story_db__to__story_dto_retrieve(story_db: StoryDB) -> StoryDTORetrieve:
        return StoryDTORetrieve(
            id=story_db.id,
            title=story_db.title,
            text=story_db.text
        )

    @staticmethod
    def story_db__to__story_dto_list(story_db: StoryDB) -> StoryDTOList:
        return StoryDTOList(
            id=story_db.id,
            title=story_db.title,
            author=UserDBDTOMapper.user_db__to__author_dto(story_db.author)
        )

    @staticmethod
    def list__story_db__to__story_dto_list(stories_db: list[StoryDB]) -> list[StoryDTOList]:
        result = []
        for i in stories_db:
            result.append(
                StoryDBDTOMapper.story_db__to__story_dto_list(i)
            )
        return result
