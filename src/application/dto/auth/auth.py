from typing import Optional

from pydantic import BaseModel
from uuid import UUID


class LoginUserDTO(BaseModel):
    username: str
    password: str


class RegisteredUserDTO(BaseModel):
    username: str
    password: str


class AuthUserDTO(BaseModel):
    id: UUID


class TokenDataDTO(BaseModel):
    username: str
    new: Optional[bool] = False
