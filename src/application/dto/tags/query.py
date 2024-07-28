from uuid import UUID

from pydantic import BaseModel


class TagDTO(BaseModel):
    id: int
    title: str


class TagStoriesDTO(TagDTO):
    stories: list[UUID]
