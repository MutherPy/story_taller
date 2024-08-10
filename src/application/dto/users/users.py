from typing import Optional

from pydantic import BaseModel
from uuid import UUID


class UserAuthorDTO(BaseModel):
    id: UUID
    username: str


class UserProfileDTO(BaseModel):
    username: str
    name: Optional[str]
    email: str
