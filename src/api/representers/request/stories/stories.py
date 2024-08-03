from pydantic import BaseModel


class StoryCreationRequestRepresenter(BaseModel):
    title: str
    text: str
    tags_ids: list[int]
