from application.bases.base_mapper import BaseMapper
from api.representers.response.users.users import UserResponseRepresenter


class UserDTORepresenterMapper(BaseMapper):
    @staticmethod
    def user_dto__to__author(user_dto) -> UserResponseRepresenter:
        return UserResponseRepresenter(
            id=user_dto.id,
            username=user_dto.username
        )
