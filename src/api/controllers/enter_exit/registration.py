from api.controllers.routers import auth_router

from fastapi import Depends

from api.representers.request.enter_exit.request import RegistrationUserRequestRepresenter
from api.representers.response.enter_exit.response import TokenResponseRepresenter
from application.facades.auth.auth_facade import AuthFacade
from providers.plugs.main_providers_plugs import main_uow_provider


# TODO add exceptions handling if user already exists
@auth_router.post('/signup', responses={200: {'model': TokenResponseRepresenter}})
async def signup(
        registration_data: RegistrationUserRequestRepresenter,
        main_uow=Depends(main_uow_provider)
):
    auth_facade = AuthFacade(uow=main_uow)
    token = await auth_facade.register_user(**registration_data.dict())
    return TokenResponseRepresenter(token=token)
