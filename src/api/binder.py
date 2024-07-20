from fastapi import FastAPI
from api.controllers import auth_router


def _bind_auth(app: FastAPI) -> None:
    app.include_router(auth_router, tags=['Auth'])


def api_binder(app: FastAPI) -> None:
    _bind_auth(app)
