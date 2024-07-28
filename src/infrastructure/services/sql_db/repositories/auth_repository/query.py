from typing import Optional

from sqlalchemy import select

from infrastructure.persistance.bases.repository import BaseRepository
from infrastructure.services.sql_db.models.users.user import UserDB

from application.mappers.auth.auth_mapper import AuthMapper
from application.dto.auth.login import LoginUserDTO
from interfaces.infrastructure.repositories.query.user import IUserQueryRepository


class UserQueryRepository(BaseRepository, IUserQueryRepository):

    auth_mapper: AuthMapper

    async def retrieve_by_username(self, username) -> Optional[LoginUserDTO]:
        stmt = select(UserDB).where(UserDB.username == username)
        user_db: Optional[UserDB] = (await self.dl_connector.scalars(stmt)).one_or_none()
        return self.auth_mapper.user_db__to__login_user_dto(user_db) if user_db else None
