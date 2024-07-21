from interfaces.infrastructure.uow import IBaseUOW
from abc import ABC


class IMainUOW(IBaseUOW, ABC):
    ...
