from interfaces.infrastructure.main_uow import IMainUOW


class BaseUseCase:
    uow: IMainUOW

    def __init__(self, uow: IMainUOW):
        self.uow: IMainUOW = uow

    async def __call__(self, *args, **kwargs):
        raise NotImplementedError
