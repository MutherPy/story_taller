from interfaces.infrastructure.uow import IBaseUOW
from abc import ABC
from interfaces.infrastructure.uows.sql_db import IDBUoW


class IMainUOW(IBaseUOW, ABC):
    db: IDBUoW
