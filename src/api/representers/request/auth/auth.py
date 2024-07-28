from pydantic import BaseModel


class LoginUserRequestRepresenter(BaseModel):
    username: str
    password: str


class RegistrationUserRequestRepresenter(BaseModel):
    username: str
    password: str
    email: str
