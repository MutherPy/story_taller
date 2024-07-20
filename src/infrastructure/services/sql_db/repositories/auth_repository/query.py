from typing import Optional

from sqlalchemy import select

from infrastructure.persistance.bases.repository import BaseRepository
from infrastructure.services.sql_db.models.users.user import User


class UserQueryRepository(BaseRepository):
    async def retrieve(self, pk) -> User:
        stmt = select(User).where(User.id == pk)
        result_obj: Optional[User] = (await self.dl_connector.scalars(stmt)).one_or_none()
        return result_obj.username if result_obj else None
