from pydantic import BaseModel


class TagDTO(BaseModel):
    id: int
    title: str
