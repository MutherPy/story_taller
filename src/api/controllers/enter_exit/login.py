from api.controllers.enter_exit.router import auth_router
from fastapi import Depends
from fastapi.responses import JSONResponse

from api.representers.request.enter_exit.request import LoginUserRequestRepresenter
from api.representers.response.enter_exit.response import TokenResponseRepresenter
from providers.plugs.facades.auth import auth_facade_provider
from interfaces.application.facades.auth_facade import IAuthFacade


@auth_router.post('/login', responses={200: {'model': TokenResponseRepresenter}, 401: {}})
async def login(
        login_data: LoginUserRequestRepresenter,
        auth_facade: IAuthFacade = Depends(auth_facade_provider)
):
    token = await auth_facade.login_user(username=login_data.username, password=login_data.password)
    if token:
        response = JSONResponse(content=TokenResponseRepresenter(token=token).model_dump())
    else:
        response = JSONResponse(content=None, status_code=401)
    return response
