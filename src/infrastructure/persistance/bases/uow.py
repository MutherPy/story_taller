from abc import abstractmethod
from typing import TypeVar, Type

from infrastructure.persistance.bases.repository import BaseRepository


SessionLike = TypeVar('SessionLike')


class BaseUOW:
    """
    Adding repos like:
    <repo_name>: Annotated[<repo_class>, <*args_to_provide>]
    """

    def __init__(self, dl_connector: SessionLike):
        self.dl_connector: SessionLike = dl_connector
        self.init_repositories()

    def init_repositories(self):
        for k, v in self.__annotations__.items():
            name = k
            _class: Type[BaseRepository] = v.__origin__
            _add_args = v.__metadata__ if v.__metadata__ else tuple()

            if issubclass(_class, BaseRepository):
                setattr(self, name, _class(self.dl_connector))

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    async def flush(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError
