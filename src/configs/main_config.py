from dataclasses import dataclass
from api.config import ApiConfig
from infrastructure.configs import SQLDBSettings


@dataclass
class Config:
    api: ApiConfig
    db: SQLDBSettings


class Secrets:
    jwt_secret: str = 'G9ueoUIl-Nh9GOgAKULpp6mpB80-hwDj6UBEh-1nEewL4Al-KJOfYm'
    passwords_secret: bytes = b'DxJWd_UHYhRZzo9IqpB_EeJlV0_GwZGBiKn_iJNclcQ='
    algorythm: str = 'HS256'
