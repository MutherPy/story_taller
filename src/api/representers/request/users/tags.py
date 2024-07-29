from pydantic import BaseModel


class UserAddTagsRequestRepresenter(BaseModel):
    tags: list[int]
