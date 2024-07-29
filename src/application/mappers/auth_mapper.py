from application.bases.base_mapper import BaseMapper

from application.dto.auth.auth import LoginUserDTO, RegisteredUserDTO, AuthUserDTO
from infrastructure.services.sql_db.models.users.user import UserDB


class AuthMapper(BaseMapper):
    @staticmethod
    def user_db__to__login_user_dto(userdb: UserDB) -> LoginUserDTO:
        return LoginUserDTO(
            username=userdb.username,
            password=userdb.password
        )

    @staticmethod
    def user_db__to__registered_user_dto(userdb: UserDB) -> RegisteredUserDTO:
        return RegisteredUserDTO(
            username=userdb.username,
            password=userdb.password
        )

    @staticmethod
    def user_db__to__auth_user_dto(user_db: UserDB) -> AuthUserDTO:
        return AuthUserDTO(id=user_db.id)
