
from api.controllers.enter_exit.router import auth_router

from fastapi import Depends

from api.representers.request.enter_exit.request import RegistrationUserRequestRepresenter
from api.representers.response.enter_exit.response import TokenResponseRepresenter
from providers.plugs.facades.auth import auth_facade_provider
from interfaces.application.facades.auth_facade import IAuthFacade


# TODO add exceptions handling if user already exists
@auth_router.post('/signup', responses={200: {'model': TokenResponseRepresenter}})
async def signup(
        registration_data: RegistrationUserRequestRepresenter,
        auth_facade: IAuthFacade = Depends(auth_facade_provider)
):
    token = await auth_facade.register_user(**registration_data.dict())
    return TokenResponseRepresenter(token=token)
