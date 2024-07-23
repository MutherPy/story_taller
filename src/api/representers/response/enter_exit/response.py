from pydantic import BaseModel


class LoginResponse200Representer(BaseModel):
    token: str


class RegistrationResponse200Representer(BaseModel):
    token: str
