from interfaces.infrastructure.main_uow import IMainUOW


class BaseUseCaseFacade:
    uow: IMainUOW

    def __init__(self, uow: IMainUOW, mapper: Mapper | None):
        self.uow: IMainUOW = uow
        super().__init__(mapper)