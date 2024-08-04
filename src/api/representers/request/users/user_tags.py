from pydantic import BaseModel


class UserTagsRequestRepresenter(BaseModel):
    tags: list[int]
