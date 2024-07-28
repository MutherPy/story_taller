from pydantic import BaseModel


class TagCreationRequestRepresenter(BaseModel):
    title: str
