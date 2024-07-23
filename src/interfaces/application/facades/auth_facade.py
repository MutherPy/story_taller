from abc import ABC


class IAuthFacade(ABC):

    async def login_user(self, username, password) -> str:
        raise NotImplementedError

    async def logout_user(self, token):
        raise NotImplementedError

    async def register_user(self, username, password, email):
        raise NotImplementedError
