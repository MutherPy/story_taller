from uuid import UUID

from fastapi import Depends

from api.controllers.routers import stories_router
from api.representers.response.stories.stories import StoryListResponseRepresenter, StoryRetrieveResponseRepresenter
from application.dto.stories.stories import StoryDTOList, StoryDTORetrieve
from providers.plugs.main_providers_plugs import main_uow_provider
from application.facades.stories.stories_facade import StoriesFacade

from api.representers.request.stories.stories import StoryCreationRequestRepresenter
from providers.plugs.auth_plugs import current_user

from api.mappers.stories_mapper import StoryDTORepresenterMapper


@stories_router.get('/story', responses={201: {'model': StoryListResponseRepresenter}, 401: {}})
async def stories_list(
        user_id=Depends(current_user),
        uow=Depends(main_uow_provider)
):
    story_facade = StoriesFacade(uow=uow)
    stories_dto: list[StoryDTOList] = (await story_facade.stories_for_user(user_id=user_id.id))
    result = StoryDTORepresenterMapper.list__story_dto_list__to__story_list(stories_dto=stories_dto)
    return result


@stories_router.get('/story/{story_id}', responses={201: {'model': StoryRetrieveResponseRepresenter}, 401: {}})
async def story_retrieve(
        story_id: UUID,
        uow=Depends(main_uow_provider)
):
    story_facade = StoriesFacade(uow=uow)
    story_dto: StoryDTORetrieve = (await story_facade.story_retrieve(story_id=story_id))
    result = StoryDTORepresenterMapper.story_dto_retrieve__to__story_retrieve(story_dto)
    return result


@stories_router.post('/story', responses={201: {'model': bool}, 401: {}})
async def create_story(
        story_data: StoryCreationRequestRepresenter,
        user_id=Depends(current_user),
        uow=Depends(main_uow_provider)
):
    story_facade = StoriesFacade(uow=uow)
    result = (await story_facade.create(
        author_id=user_id.id, title=story_data.title,
        text=story_data.text, tags_ids=story_data.tags_ids)
              )
    return result

