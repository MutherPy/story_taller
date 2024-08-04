from pydantic import BaseModel
from uuid import UUID


class UserResponseRepresenter(BaseModel):
    id: UUID
    username: str
