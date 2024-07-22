from typing import Annotated

from api.controllers.enter_exit.router import auth_router
from fastapi import Depends

from providers.plugs.facades.auth import auth_facade_provider
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from interfaces.application.facades.auth_facade import IAuthFacade

security = HTTPBasic()


@auth_router.post('/login')
async def login(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
        auth_facade: IAuthFacade = Depends(auth_facade_provider)
):
    user = await auth_facade.login_user(username=credentials.username, password=credentials.password)
    print(user)
    return 'token' if user else 'sosi'
