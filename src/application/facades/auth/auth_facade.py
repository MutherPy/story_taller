from application.bases.base_facade import BaseUseCaseFacade


from application.usecases.auth.login import LogInUseCase
from application.usecases.auth.registration import RegistrationUseCase


class AuthFacade(BaseUseCaseFacade):
    async def login_user(self, username, password) -> str:
        return await LogInUseCase(self.uow)(username, password)

    async def register_user(self, username, password, email):
        return await RegistrationUseCase(self.uow)(username, password, email)

