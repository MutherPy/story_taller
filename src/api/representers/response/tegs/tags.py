from pydantic import BaseModel


class TagResponseRepresenter(BaseModel):
    id: int
    title: str
