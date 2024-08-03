from infrastructure.persistance.bases.repository import BaseRepository

from infrastructure.services.sql_db.models.users.user import UserDB
from infrastructure.services.sql_db.models.many_to_many.users_tags import users_to_tags_association_table
from application.mappers.auth_mapper import AuthMapper
from application.dto.auth.auth import RegisteredUserDTO
from sqlalchemy import insert


class UserCommandRepository(BaseRepository):

    auth_mapper: AuthMapper

    async def create_new_user(self, username: str, password: str, email: str) -> RegisteredUserDTO:
        userdb = await self._create(username=username, password=password, email=email)
        return self.auth_mapper.user_db__to__registered_user_dto(userdb=userdb)

    async def _create(self, username: str, password: str, email: str) -> UserDB:
        user = UserDB(username=username, email=email, password=password)
        self.dl_connector.add(user)
        await self.dl_connector.flush()
        return user

    async def add_user_tags(self, user_id: str, new_tags: list[int]) -> bool:
        for tag_id in new_tags:
            stmt = insert(users_to_tags_association_table).values(user_id=user_id, tag_id=tag_id)
            await self.dl_connector.execute(stmt)
        await self.dl_connector.flush()
        return True

