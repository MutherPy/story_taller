from infrastructure.persistance.bases.repository import BaseRepository

from infrastructure.services.sql_db.models.users.user import UserDB
from infrastructure.services.sql_db.models.common.tag import TagDB
from application.mappers.auth_mapper import AuthMapper


class UserCommandRepository(BaseRepository):

    auth_mapper: AuthMapper

    async def create_new_user(self, username: str, password: str, email: str):
        userdb = await self._create(username=username, password=password, email=email)
        return self.auth_mapper.user_db__to__registered_user_dto(userdb=userdb)

    async def _create(self, username: str, password: str, email: str):
        user = UserDB(username=username, email=email, password=password)
        self.dl_connector.add(user)
        await self.dl_connector.flush()
        return user

    # TODO consider how to do it in more proper way. likse Q operations not inside C operations
    async def add_user_tags(self, user_id, new_tags) -> bool:
        from sqlalchemy.sql.expression import select
        stmt = select(UserDB).where(UserDB.id == user_id)
        user_db: UserDB = (await self.dl_connector.scalars(stmt)).one_or_none()
        if user_db:
            # for tag_id in new_tags:
            tag_db_stmt = select(TagDB).where(TagDB.id.in_(new_tags))
            tags_db = (await self.dl_connector.scalars(tag_db_stmt)).all()
            for tag in tags_db:
                user_db.tags.append(tag)
            self.dl_connector.add(user_db)
            await self.dl_connector.flush()
        return True

