from application.mappers.tags_mapper import TagsMapper
from infrastructure.persistance.bases.repository import BaseRepository
from application.dto.tags.query import TagDTO
from infrastructure.services.sql_db.models.common.tag import TagDB


class TagsCommandRepository(BaseRepository):
    tags_mapper: TagsMapper

    async def create(self, tag_title: str) -> TagDTO:
        new_tag_db = TagDB(title=tag_title)
        self.dl_connector.add(new_tag_db)
        await self.dl_connector.flush()
        return self.tags_mapper.tag_db__to__tag_dto(new_tag_db)

