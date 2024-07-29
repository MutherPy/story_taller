from application.bases.base_facade import BaseUseCaseFacade

from application.usecases.users.users import AddUserTags


class UsersFacade(BaseUseCaseFacade):
    async def add_tags(self, user_id, tags_to_add: list[int]):
        return await AddUserTags(self.uow)(user_id=user_id, tags_to_add=tags_to_add)
