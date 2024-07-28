from application.bases.base_mapper import BaseMapper
from infrastructure.services.sql_db.models.common.tag import TagDB
from application.dto.tags.tags import TagDTO


class TagsDBDTOMapper(BaseMapper):

    @staticmethod
    def tag_db__to__tag_dto(tag_db: TagDB) -> TagDTO:
        return TagDTO(id=tag_db.id, title=tag_db.title)

    @staticmethod
    def list__tag_db__to__tag_dto(tags_db: list[TagDB] | None) -> list[TagDTO]:
        if not tags_db:
            return []
        result = []
        for tag_db in tags_db:
            result.append(TagsDBDTOMapper.tag_db__to__tag_dto(tag_db))
        return result
