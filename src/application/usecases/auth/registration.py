from application.bases.base_usecase import BaseUseCase
from application.dto.auth.registration import RegisteredUserDTO
from infrastructure.services.auth import validator, id_provider


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
