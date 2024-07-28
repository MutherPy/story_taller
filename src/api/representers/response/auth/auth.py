from pydantic import BaseModel


class TokenResponseRepresenter(BaseModel):
    token: str

