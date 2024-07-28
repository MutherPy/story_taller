from application.bases.base_mapper import BaseMapper
from application.dto.tags.tags import TagDTO
from api.representers.response.tags.tags import TagResponseRepresenter, TagListResponseRepresenter


class TagDTORepresenterMapper(BaseMapper):
    @staticmethod
    def tag_dto__to__tag(tag: TagDTO) -> TagResponseRepresenter:
        return TagResponseRepresenter(id=tag.id, title=tag.title)

    @staticmethod
    def list__tag_dto__to__tag(tag_list: list[TagDTO]) -> TagListResponseRepresenter:
        tags = []
        for tag in tag_list:
            tags.append(TagDTORepresenterMapper.tag_dto__to__tag(tag))
        return TagListResponseRepresenter(tags=tags)
