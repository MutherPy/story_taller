from application.bases.base_facade import BaseUseCaseFacade

from application.usecases.stories.stories import CreateStory


class StoriesFacade(BaseUseCaseFacade):
    async def create(self, author_id, title, text, tags_ids):
        return await CreateStory(self.uow)(author_id, title, text, tags_ids)
