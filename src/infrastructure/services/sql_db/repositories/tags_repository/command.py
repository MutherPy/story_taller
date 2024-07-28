from application.mappers.tags_mapper import TagsMapper
from infrastructure.persistance.bases.repository import BaseRepository


class TagsCommandRepository(BaseRepository):
    tags_mapper: TagsMapper

