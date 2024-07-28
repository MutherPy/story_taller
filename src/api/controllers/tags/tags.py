from api.controllers.routers import tags_router
from fastapi import Depends

from api.representers.request.tags.tags import TagCreationRequestRepresenter
from api.representers.response.tags.tags import TagResponseRepresenter
from application.facades.tags.tags_facade import TagsFacade
from providers.plugs.main_providers_plugs import main_uow_provider


@tags_router.get('/tag', responses={200: {'model': list[TagResponseRepresenter]}, 401: {}})
async def tags_list(uow=Depends(main_uow_provider)):
    tags_facade = TagsFacade(uow=uow)
    tags_list_result = (await tags_facade.list())
    return tags_list_result


@tags_router.post('/tag', responses={200: {'model': TagResponseRepresenter}, 401: {}})
async def tag_create(tag_name: TagCreationRequestRepresenter, uow=Depends(main_uow_provider)):
    tags_facade = TagsFacade(uow=uow)
    new_tag = (await tags_facade.create(tag_name.title))
    return new_tag


