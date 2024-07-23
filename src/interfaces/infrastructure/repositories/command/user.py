from abc import ABC


class IUserCommandRepository(ABC):

    async def create_new_user(self, username: str, password: str, email: str):
        raise NotImplementedError

    async def _create(self, username: str, password: str, email: str):
        raise NotImplementedError

