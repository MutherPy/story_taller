from application.bases.base_facade import BaseUseCaseFacade

from application.usecases.tags.list import TagsList


class TagsFacade(BaseUseCaseFacade):
    async def list(self):
        return await TagsList(self.uow)()
