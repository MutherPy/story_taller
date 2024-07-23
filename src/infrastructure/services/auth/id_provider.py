import jwt
from configs.main_config import Secrets


class IdentityProvider:
    @staticmethod
    def create_token(data: dict) -> str:
        return jwt.encode(data, key=Secrets.jwt_secret, algorithm=Secrets.algorythm)

    @staticmethod
    def validate_token(token: str) -> dict:
        return jwt.decode(token, key=Secrets.jwt_secret, algorithms=[Secrets.algorythm])
