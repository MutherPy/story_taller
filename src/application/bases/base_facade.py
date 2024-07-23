from infrastructure.persistance.main_uow import MainUOW
from interfaces.infrastructure.main_uow import IMainUOW


class BaseUseCaseFacade:
    uow: MainUOW

    def __init__(self, uow: IMainUOW):
        self.uow: IMainUOW = uow
