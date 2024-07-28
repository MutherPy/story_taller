import uvicorn
from fastapi import FastAPI

from app_initializer import app_initializer
from configs.config_loader import LoadedConfig


def app():
    initialized_app = app_initializer(FastAPI, LoadedConfig)
    return initialized_app


if __name__ == "__main__":
    uvicorn.run(
        LoadedConfig.api.APP,
        host=LoadedConfig.api.HOST,
        port=LoadedConfig.api.PORT,
        log_level=LoadedConfig.api.ASGI_LOG_LEVEL,
        reload=True,
        reload_includes='*.py'
    )
