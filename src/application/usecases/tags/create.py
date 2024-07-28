from application.bases.base_usecase import BaseUseCase
from application.dto.tags.query import TagDTO


class CreateTag(BaseUseCase):
    async def __call__(self, tag_title: str) -> TagDTO:
        try:
            new_tag_dto = await self.uow.db.tags_c_rep.create(tag_title=tag_title)
            await self.uow.commit()
            return new_tag_dto
        except Exception:
            await self.uow.rollback()
            raise

