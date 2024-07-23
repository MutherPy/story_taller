from fastapi import FastAPI
from api.middlewares.auth_middleware import AuthMiddleware


def bind_middlewares(app: FastAPI):
    app.add_middleware(
        AuthMiddleware,
        public_paths=['/login', '/signup']
    )
