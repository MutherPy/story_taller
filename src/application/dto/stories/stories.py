from pydantic import BaseModel

from uuid import UUID

from application.dto.tags.tags import TagDTO
from application.dto.users.users import UserAuthorDTO
from application.choises.story import StoryStatus

from datetime import datetime


class StoryDTOList(BaseModel):
    id: UUID
    title: str
    author: UserAuthorDTO


class StoryDTORetrieve(StoryDTOList):
    text: str
    tags: list[TagDTO]

    status: StoryStatus

    creation_date: datetime
