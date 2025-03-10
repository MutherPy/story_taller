from application.bases.base_usecase import BaseUseCase


class AddUserTags(BaseUseCase):
    async def __call__(self, user_id, tags_to_add: list[int]):
        added = await self.uow.db.user_c_rep.add_user_tags(user_id, tags_to_add)
        await self.uow.commit()
        return added


class UserProfile(BaseUseCase):
    async def __call__(self, user_id):
        user_profile_dto = await self.uow.db.user_q_rep.retrieve_profile_info(user_id=user_id)
        return user_profile_dto
