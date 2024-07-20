from logging import getLogger

from configs.main_config import Config
from api.config import ApiConfig
from infrastructure.configs import SQLDBSettings


def config_loader() -> Config:
    log = getLogger()
    log.info('Configs loaded')

    return Config(
        api=ApiConfig(),
        db=SQLDBSettings()
    )


LoadedConfig = config_loader()
