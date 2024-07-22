from infrastructure.persistance.bases.repository import BaseRepository

from sqlalchemy import select

from infrastructure.services.sql_db.models.users.user import User


class UserCommandRepository(BaseRepository):
    async def create_user(self, username, password, email):
        user = User(username=username, email=email, password=password)
        self.dl_connector.add(user)
        await self.dl_connector.flush()
        return user.id

