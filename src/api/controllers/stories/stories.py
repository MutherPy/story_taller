from fastapi import Depends

from api.controllers.routers import stories_router
from providers.plugs.main_providers_plugs import main_uow_provider
from application.facades.stories.stories_facade import StoriesFacade

from api.representers.request.stories.stories import StoryCreationRequestRepresenter
from providers.plugs.auth_plugs import current_user


@stories_router.post('/story', responses={201: {'model': bool}, 401: {}})
async def create_story(
        story_data: StoryCreationRequestRepresenter,
        user_id=Depends(current_user),
        uow=Depends(main_uow_provider)
):
    story_facade = StoriesFacade(uow=uow)
    result = (await story_facade.create(author_id=user_id.id, **story_data.model_dump()))
    return result

