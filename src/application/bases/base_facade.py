from infrastructure.persistance.main_uow import MainUOW


class BaseUseCaseFacade:
    uow: MainUOW

    def __init__(self, uow: MainUOW):
        self.uow: MainUOW = uow
