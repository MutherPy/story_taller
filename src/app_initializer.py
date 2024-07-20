from typing import Type

from fastapi import FastAPI
from configs.main_config import Config
from api.binder import api_binder
from providers.binder import bind_providers


def app_initializer(app_class: Type[FastAPI], configs: Config) -> FastAPI:
    app = app_class(
        debug=configs.api.APP_DEBUG
    )
    bind_providers(app)
    api_binder(app)
    return app
