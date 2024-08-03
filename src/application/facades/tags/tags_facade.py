from application.bases.base_facade import BaseUseCaseFacade

from application.usecases.tags.tags import ListTag, CreateTag, UserTags


class TagsFacade(BaseUseCaseFacade):
    async def list(self):
        return await ListTag(self.uow)()

    async def create(self, tag_title: str):
        return await CreateTag(self.uow)(tag_title=tag_title)

    async def user_tags(self, user_id):
        return await UserTags(self.uow)(user_id=user_id)
