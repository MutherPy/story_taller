from application.mappers.tags_mapper import TagsDBDTOMapper
from infrastructure.persistance.bases.repository import BaseRepository
from infrastructure.services.sql_db.models.common.tag import TagDB
from sqlalchemy import select

from application.dto.tags.tags import TagDTO


class TagsQueryRepository(BaseRepository):
    tags_mapper: TagsDBDTOMapper

    async def get_all_tags(self) -> list[TagDTO]:
        stmt = select(TagDB)
        tags_db = (await self.dl_connector.scalars(stmt))
        result = self.tags_mapper.list__tag_db__to__tag_dto(tags_db=tags_db)
        return result
