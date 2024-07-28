from interfaces.type_vars import SessionLike
from application.bases.base_mapper import BaseMapper


class BaseRepository:
    """Base for repositories for Infrastructure Layer"""

    def __init__(self, dl_connector: SessionLike):
        self.dl_connector = dl_connector
        self.__init_mappers()

    def __init_mappers(self):
        for k, v in self.__annotations__.items():
            if issubclass(v, BaseMapper):
                setattr(self, k, v)
