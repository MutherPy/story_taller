from infrastructure.persistance.main_uow import MainUOW


class BaseUseCase:
    uow: MainUOW

    def __init__(self, uow: MainUOW):
        self.uow: MainUOW = uow

    async def __call__(self, *args, **kwargs):
        raise NotImplementedError
