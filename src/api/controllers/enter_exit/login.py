from typing import Annotated

from api.controllers.enter_exit.router import auth_router
from fastapi import Depends
from fastapi.responses import JSONResponse

from api.representers.response.enter_exit.response import LoginResponse200Representer
from providers.plugs.facades.auth import auth_facade_provider
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from interfaces.application.facades.auth_facade import IAuthFacade

security = HTTPBasic()


@auth_router.post('/login', responses={200: {'model': LoginResponse200Representer}, 401: {}})
async def login(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
        auth_facade: IAuthFacade = Depends(auth_facade_provider)
):
    token = await auth_facade.login_user(username=credentials.username, password=credentials.password)
    if token:
        response = JSONResponse(content=LoginResponse200Representer(token=token).model_dump())
    else:
        response = JSONResponse(content=None, status_code=401)
    return response
