from fastapi import FastAPI
from api.controllers.routers import auth_router, tags_router
from api.middlewares.auth_middleware import AuthMiddleware
from fastapi import APIRouter


def _bind_auth(app: FastAPI) -> None:
    app.include_router(auth_router, tags=['Auth'])


def _bind_api(app: FastAPI) -> None:
    api = APIRouter(prefix='/api')
    api.include_router(tags_router, tags=['Tags'])
    app.include_router(api)


def binder_routers(app: FastAPI) -> None:
    _bind_auth(app)
    _bind_api(app)


def bind_middlewares(app: FastAPI):
    app.add_middleware(
        AuthMiddleware,
        public_paths=['/login', '/signup']
    )
