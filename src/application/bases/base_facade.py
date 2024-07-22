from interfaces.infrastructure.main_uow import IMainUOW


class BaseUseCaseFacade:
    uow: IMainUOW

    def __init__(self, uow: IMainUOW):
        self.uow: IMainUOW = uow
