from application.bases.base_usecase import BaseUseCase


class TagsList(BaseUseCase):
    async def __call__(self):
        return await self.uow.db.tags_q_rep.get_all_tags()
