from pydantic import BaseModel


class RegistrationUserRequestRepresenter(BaseModel):
    username: str
    password: str
    email: str
