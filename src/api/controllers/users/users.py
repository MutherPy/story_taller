
from api.controllers.routers import user_router
from fastapi import Depends

from api.representers.request.users.user_tags import UserTagsRequestRepresenter
from providers.plugs.auth_plugs import current_user
from providers.plugs.main_providers_plugs import main_uow_provider
from application.facades.users.users_facade import UsersFacade

from application.dto.auth.auth import AuthUserDTO


@user_router.post('/user/add_tags', responses={200: {"model": bool}, 401: {}})
async def add_user_tags(
        adding_tags: UserTagsRequestRepresenter,
        uow=Depends(main_uow_provider),
        user_id: AuthUserDTO = Depends(current_user)
):
    users_facade = UsersFacade(uow=uow)
    is_added: bool = await users_facade.add_tags(user_id=user_id.id, tags_to_add=adding_tags.tags)
    return is_added
