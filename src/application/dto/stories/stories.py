from pydantic import BaseModel

from uuid import UUID

from application.dto.tags.tags import TagDTO


class StoryDTOList(BaseModel):
    id: UUID
    title: str
    text: str


class StoryDTORetrieve(StoryDTOList):
    tags: list[TagDTO]

