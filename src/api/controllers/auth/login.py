from api.controllers.routers import auth_router
from fastapi import Depends
from fastapi.responses import JSONResponse

from api.representers.request.auth.auth import LoginUserRequestRepresenter
from api.representers.response.auth.auth import TokenResponseRepresenter
from application.facades.auth.auth_facade import AuthFacade
from providers.plugs.main_providers_plugs import main_uow_provider


@auth_router.post('/login', responses={200: {'model': TokenResponseRepresenter}, 401: {}})
async def login(
        login_data: LoginUserRequestRepresenter,
        main_uow=Depends(main_uow_provider)
):
    auth_facade = AuthFacade(uow=main_uow)
    token = await auth_facade.login_user(username=login_data.username, password=login_data.password)
    if token:
        response = JSONResponse(content=TokenResponseRepresenter(token=token).model_dump())
    else:
        response = JSONResponse(content=None, status_code=401)
    return response
