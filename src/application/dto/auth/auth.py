from pydantic import BaseModel


class LoginUserDTO(BaseModel):
    username: str
    password: str


class RegisteredUserDTO(BaseModel):
    username: str
    password: str
