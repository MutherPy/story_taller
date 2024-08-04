from application.bases.base_mapper import BaseMapper
from infrastructure.services.sql_db.models.users.user import UserDB
from application.dto.users.users import UserDTO


class UserDBDTOMapper(BaseMapper):
    @staticmethod
    def user_db__to__author_dto(user_db: UserDB) -> UserDTO:
        return UserDTO(
            id=user_db.id,
            username=user_db.username
        )
