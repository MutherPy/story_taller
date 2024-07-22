from typing import Optional

from sqlalchemy import select

from infrastructure.persistance.bases.repository import BaseRepository
from infrastructure.services.sql_db.models.users.user import User


class UserQueryRepository(BaseRepository):

    async def retrieve_by_username_and_password(self, username, password):
        stmt = select(User).where(User.username == username).where(User.password == password)
        result_obj: Optional[User] = (await self.dl_connector.scalars(stmt)).one_or_none()
        return result_obj.username if result_obj else None
