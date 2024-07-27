from fastapi import FastAPI
from api.controllers.routers import auth_router


def _bind_auth(app: FastAPI) -> None:
    app.include_router(auth_router, tags=['Auth'])


def binder_routers(app: FastAPI) -> None:
    _bind_auth(app)
