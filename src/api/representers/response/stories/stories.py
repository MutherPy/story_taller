from pydantic import BaseModel

from uuid import UUID
from datetime import datetime


from api.representers.response.tags.tags import TagResponseRepresenter
from api.representers.response.users.users import UserAuthorResponseRepresenter

from application.choises.story import StoryStatus


class StoryResponseRepresenter(BaseModel):
    id: UUID
    title: str
    author: UserAuthorResponseRepresenter


class StoryRetrieveResponseRepresenter(StoryResponseRepresenter):
    text: str
    tags: list[TagResponseRepresenter]
    creation_date: datetime
    status: StoryStatus


class StoryListResponseRepresenter(BaseModel):
    stories: list[StoryResponseRepresenter]
