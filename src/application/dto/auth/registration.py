from pydantic import BaseModel


class RegisteredUserDTO(BaseModel):
    username: str
    password: str
