from dataclasses import dataclass
from api.config import ApiConfig
from infrastructure.configs import SQLDBSettings


@dataclass
class Config:
    api: ApiConfig
    db: SQLDBSettings

