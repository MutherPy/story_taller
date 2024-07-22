from typing import Annotated

from api.controllers.enter_exit.router import auth_router

from fastapi import Depends, Body, Request

from providers.plugs.facades.auth import auth_facade_provider
from interfaces.application.facades.auth_facade import IAuthFacade

import json


@auth_router.post('/registration')
async def registration(request: Request, auth_facade: IAuthFacade = Depends(auth_facade_provider)):
    body = await request.json()
    user_id = await auth_facade.register_user(**body)
    return user_id
