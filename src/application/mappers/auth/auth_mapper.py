from application.bases.base_mapper import BaseMapper

from application.dto.auth.login import LoginUserDTO
from application.dto.auth.registration import RegisteredUserDTO
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
