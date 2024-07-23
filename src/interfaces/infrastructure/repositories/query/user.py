from abc import ABC


class IUserQueryRepository(ABC):

    async def retrieve_by_username(self, username):
        raise NotImplementedError
