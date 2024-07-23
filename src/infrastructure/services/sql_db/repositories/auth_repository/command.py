from infrastructure.persistance.bases.repository import BaseRepository

from infrastructure.services.sql_db.models.users.user import UserDB
from interfaces.infrastructure.repositories.command.user import IUserCommandRepository
from application.mappers.auth.auth_mapper import AuthMapper


class UserCommandRepository(BaseRepository, IUserCommandRepository):

    auth_mapper = AuthMapper

    async def create_new_user(self, username: str, password: str, email: str):
        userdb = await self._create(username=username, password=password, email=email)
        return self.auth_mapper.user_db__to__registered_user_dto(userdb=userdb)

    async def _create(self, username: str, password: str, email: str):
        user = UserDB(username=username, email=email, password=password)
        self.dl_connector.add(user)
        await self.dl_connector.flush()
        return user
