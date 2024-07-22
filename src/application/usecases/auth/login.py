from application.bases.base_usecase import BaseUseCase


class LogInUseCase(BaseUseCase):
    async def __call__(self, username: str, password: str):
        user = await self.uow.db.user_q_rep.retrieve_by_username_and_password(username=username, password=password)
        return user


class LogOutUseCase(BaseUseCase):
    async def __call__(self, token: str):
        ...
