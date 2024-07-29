from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from api.controllers.routers import auth_router, tags_router, user_router
from api.middlewares.auth_middleware import AuthMiddleware
from fastapi import APIRouter


def _bind_auth(app: FastAPI) -> None:
    app.include_router(auth_router, tags=['Auth'])


def _bind_api(app: FastAPI) -> None:
    sec = HTTPBearer()
    api = APIRouter(prefix='/api', dependencies=[Depends(sec)])
    api.include_router(tags_router, tags=['Tags'])
    api.include_router(user_router, tags=['Users'])
    app.include_router(api)


def binder_routers(app: FastAPI) -> None:
    _bind_auth(app)
    _bind_api(app)


def bind_middlewares(app: FastAPI):
    app.add_middleware(
        AuthMiddleware,
        public_paths=['/login', '/signup']
    )
