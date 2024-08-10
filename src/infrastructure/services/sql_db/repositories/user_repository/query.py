from typing import Optional

from sqlalchemy import select

from infrastructure.persistance.bases.repository import BaseRepository
from infrastructure.services.sql_db.models.users.user import UserDB

from application.mappers.auth_mapper import AuthUserDBDTOMapper
from application.mappers.users_mapper import UserDBDTOMapper
from application.dto.auth.auth import LoginUserDTO, AuthUserDTO
from application.dto.users.users import UserProfileDTO


class UserQueryRepository(BaseRepository):

    auth_mapper: AuthUserDBDTOMapper
    user_mapper: UserDBDTOMapper

    async def retrieve_by_username(self, username) -> Optional[LoginUserDTO]:
        stmt = select(UserDB).where(UserDB.username == username)
        user_db: Optional[UserDB] = (await self.dl_connector.scalars(stmt)).one_or_none()
        return self.auth_mapper.user_db__to__login_user_dto(user_db) if user_db else None

    async def retrieve_id_by_username(self, username) -> Optional[AuthUserDTO]:
        stmt = select(UserDB).where(UserDB.username == username)
        user_db: Optional[UserDB] = (await self.dl_connector.scalars(stmt)).one_or_none()
        return self.auth_mapper.user_db__to__auth_user_dto(user_db) if user_db else None

    async def retrieve_profile_info(self, user_id) -> UserProfileDTO:
        stmt = select(UserDB).where(UserDB.id == user_id)
        user_db: UserDB = (await self.dl_connector.scalar(stmt))
        return self.user_mapper.user_db__to__user_profile_dto(user_db)
