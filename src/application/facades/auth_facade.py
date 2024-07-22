from application.bases.base_facade import BaseUseCaseFacade
from interfaces.application.facades.auth_facade import IAuthFacade


from application.usecases.auth.login import LogInUseCase, LogOutUseCase
from application.usecases.auth.registration import RegistrationUseCase


class AuthFacade(BaseUseCaseFacade, IAuthFacade):
    async def login_user(self, username, password):
        return await LogInUseCase(self.uow)(username, password)

    async def logout_user(self, token):
        return await LogOutUseCase(self.uow)(token)

    async def register_user(self, username, password, email):
        return await RegistrationUseCase(self.uow)(username, password, email)

