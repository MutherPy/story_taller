from application.bases.base_usecase import BaseUseCase


class RegistrationUseCase(BaseUseCase):
    async def __call__(self, username, password, email):
        user_id = await self.uow.db.user_c_rep.create_user(username=username, email=email, password=password)
        await self.uow.commit()
        return user_id
