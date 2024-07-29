import jwt

from application.dto.auth.auth import TokenDataDTO
from configs.main_config import Secrets


class IdentityProvider:
    @staticmethod
    def create_token(data: TokenDataDTO) -> str:
        return jwt.encode(data.model_dump(), key=Secrets.jwt_secret, algorithm=Secrets.algorythm)

    @staticmethod
    def validate_token(token: str) -> TokenDataDTO:
        decoded_token = jwt.decode(token, key=Secrets.jwt_secret, algorithms=[Secrets.algorythm])
        return TokenDataDTO.parse_obj(decoded_token)
