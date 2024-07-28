from application.bases.base_usecase import BaseUseCase
from infrastructure.services.auth import validator, id_provider
from application.dto.auth.auth import LoginUserDTO, RegisteredUserDTO
from typing import Optional


class LogInUseCase(BaseUseCase):
    async def __call__(self, username: str, password: str) -> str:
        user_dto: Optional[LoginUserDTO] = await self.uow.db.user_q_rep.retrieve_by_username(username=username)
        token: Optional[str] = None
        if user_dto:
            if validator.PasswordsService.validate_password(password=password, storing_password=user_dto.password):
                token = id_provider.IdentityProvider.create_token({'user': user_dto.username})
        return token


class RegistrationUseCase(BaseUseCase):
    async def __call__(self, username: str, password: str, email: str):
        encr_password = validator.PasswordsService.encrypt_password(password)
        try:
            registered_user_dto: RegisteredUserDTO = await self.uow.db.user_c_rep.create_new_user(
                username=username,
                email=email,
                password=encr_password
            )
            await self.uow.commit()
        except Exception:
            await self.uow.rollback()
            raise
        return id_provider.IdentityProvider.create_token({'user': registered_user_dto.username, 'new': True})

