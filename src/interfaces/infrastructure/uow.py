from abc import ABC, abstractmethod
from interfaces.type_vars import SessionLike


class IBaseUOW(ABC):
    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class IBaseCommonUOW(IBaseUOW, ABC):
    dl_connector: SessionLike
