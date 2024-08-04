from pydantic import BaseModel
from uuid import UUID


class UserDTO(BaseModel):
    id: UUID
    username: str
