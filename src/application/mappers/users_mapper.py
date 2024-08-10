from application.bases.base_mapper import BaseMapper
from infrastructure.services.sql_db.models.users.user import UserDB
from application.dto.users.users import UserAuthorDTO, UserProfileDTO


class UserDBDTOMapper(BaseMapper):
    @staticmethod
    def user_db__to__author_dto(user_db: UserDB) -> UserAuthorDTO:
        return UserAuthorDTO(
            id=user_db.id,
            username=user_db.username
        )

    @staticmethod
    def user_db__to__user_profile_dto(user_db: UserDB) -> UserProfileDTO:
        return UserProfileDTO(
            username=user_db.username,
            name=user_db.name,
            email=user_db.email
        )
