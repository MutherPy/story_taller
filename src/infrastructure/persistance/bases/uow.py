from abc import ABC
from typing import Type

from infrastructure.persistance.bases.repository import BaseRepository

from interfaces.type_vars import SessionLike
from interfaces.infrastructure.uow import IBaseCommonUOW
from interfaces.infrastructure.main_uow import IMainUOW


class BaseUOW(IBaseCommonUOW, ABC):
    """
    Adding repos like:
    <repo_name>: Annotated[<repo_class>, <*args_to_provide>]
    """

    def __init__(self, dl_connector: SessionLike):
        self.dl_connector: SessionLike = dl_connector
        self.__init_repositories()

    def __init_repositories(self):
        for k, v in self.__annotations__.items():
            name = k
            _class: Type[BaseRepository] = v.__origin__
            _add_args = v.__metadata__ if v.__metadata__ else tuple()

            if issubclass(_class, BaseRepository):
                setattr(self, name, _class(self.dl_connector))


class BaseMainUOW(IMainUOW, ABC):
    def __init__(self, **common_uow_instances):
        self._uows = []
        self.__init_uows(instances=common_uow_instances)

    def __init_uows(self, instances: dict[str, IBaseCommonUOW]):
        for k, v in self.__annotations__.items():
            name = k
            _class: Type[IBaseCommonUOW] = v
            if inst := instances.get(name):
                if isinstance(inst, _class):
                    setattr(self, name, inst)

    async def commit(self):
        for uow in self._uows:
            await uow.commit()

    async def rollback(self):
        for uow in self._uows:
            await uow.rollback()
