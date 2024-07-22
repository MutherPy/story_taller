from interfaces.infrastructure.uow import IBaseUOW, IBaseCommonUOW
from abc import ABC


class IMainUOW(IBaseUOW, ABC):
    db: IBaseCommonUOW
