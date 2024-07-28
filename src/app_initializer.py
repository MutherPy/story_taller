from typing import Type

from fastapi import FastAPI

from configs.main_config import Config
from api.binder import binder_routers, bind_middlewares
from providers.binder import bind_providers


def app_initializer(app_class: Type[FastAPI], configs: Config) -> FastAPI:
    app = app_class(
        debug=configs.api.APP_DEBUG

    )
    bind_providers(app)
    # bind_middlewares(app)
    binder_routers(app)
    return app
