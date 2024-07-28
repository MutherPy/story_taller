from application.bases.base_facade import BaseUseCaseFacade

from application.usecases.tags.tags import ListTag, CreateTag


class TagsFacade(BaseUseCaseFacade):
    async def list(self):
        return await ListTag(self.uow)()

    async def create(self, tag_title: str):
        return await CreateTag(self.uow)(tag_title=tag_title)
