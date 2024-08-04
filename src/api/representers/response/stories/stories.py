from pydantic import BaseModel

from uuid import UUID

from api.representers.response.tags.tags import TagResponseRepresenter
from api.representers.response.users.users import UserResponseRepresenter


class StoryResponseRepresenter(BaseModel):
    id: UUID
    title: str
    author: UserResponseRepresenter


class StoryRetrieveResponseRepresenter(StoryResponseRepresenter):
    text: str
    tags: list[TagResponseRepresenter]


class StoryListResponseRepresenter(BaseModel):
    stories: list[StoryResponseRepresenter]
