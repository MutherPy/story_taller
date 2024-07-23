from application.bases.base_usecase import BaseUseCase
from infrastructure.services.auth import validator, id_provider
from application.dto.auth.login import LoginUserDTO
from typing import Optional


class LogInUseCase(BaseUseCase):
    async def __call__(self, username: str, password: str) -> str:
        user: Optional[LoginUserDTO] = await self.uow.db.user_q_rep.retrieve_by_username(username=username)
        token: Optional[str] = None
        if user:
            if validator.PasswordsService.validate_password(password=password, storing_password=user.password):
                token = id_provider.IdentityProvider.create_token({'user': username})
        return token


class LogOutUseCase(BaseUseCase):
    async def __call__(self, token: str):
        ...
