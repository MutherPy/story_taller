from application.bases.base_facade import BaseUseCaseFacade

from application.usecases.tags import list, create


class TagsFacade(BaseUseCaseFacade):
    async def list(self):
        return await list.TagsList(self.uow)()

    async def create(self, tag_title: str):
        return await create.CreateTag(self.uow)(tag_title=tag_title)
