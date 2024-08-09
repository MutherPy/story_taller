from api.mappers.users_mapper import UserDTORepresenterMapper
from api.mappers.tags_mapper import TagDTORepresenterMapper
from api.representers.response.stories.stories import (
    StoryResponseRepresenter,
    StoryListResponseRepresenter,
    StoryRetrieveResponseRepresenter
)
from application.bases.base_mapper import BaseMapper
from application.dto.stories.stories import StoryDTOList, StoryDTORetrieve


class StoryDTORepresenterMapper(BaseMapper):
    @staticmethod
    def list__story_dto_list__to__story_list(stories_dto: list[StoryDTOList]) -> StoryListResponseRepresenter:
        stories = []
        for story_dto in stories_dto:
            stories.append(
                StoryDTORepresenterMapper.story_dto_list__to__story_list(
                    story_dto
                )
            )

        return StoryListResponseRepresenter(
            stories=stories
        )

    @staticmethod
    def story_dto_list__to__story_list(story_dto: StoryDTOList) -> StoryResponseRepresenter:
        author = UserDTORepresenterMapper.user_dto__to__author(user_dto=story_dto.author)
        return StoryResponseRepresenter(
            id=story_dto.id,
            title=story_dto.title,
            author=author
        )

    @staticmethod
    def story_dto_retrieve__to__story_retrieve(story_dto: StoryDTORetrieve) -> StoryRetrieveResponseRepresenter:
        data: StoryResponseRepresenter = StoryDTORepresenterMapper.story_dto_list__to__story_list(story_dto=story_dto)
        tags = TagDTORepresenterMapper.list__tag_dto__to__list_tags(story_dto.tags)
        return StoryRetrieveResponseRepresenter(
            id=data.id,
            title=data.title,
            author=data.author,
            text=story_dto.text,
            tags=tags,
            creation_date=story_dto.creation_date
        )

