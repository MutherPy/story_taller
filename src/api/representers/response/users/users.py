from typing import Optional

from pydantic import BaseModel
from uuid import UUID


class UserAuthorResponseRepresenter(BaseModel):
    id: UUID
    username: str


class UserProfileResponseRepresenter(BaseModel):
    username: str
    name: Optional[str]
    email: str
