from fastapi import Depends
from providers.plugs.infrastructure_plugs import main_uow_provider

from application.facades.auth.auth_facade import AuthFacade


# auth_facade_provider
def get_auth_facade_provider(uow=Depends(main_uow_provider)):
    return AuthFacade(uow=uow)
