from interfaces.type_vars import SessionLike


class BaseRepository:
    """Base for repositories for Infrastructure Layer"""

    def __init__(self, dl_connector: SessionLike):
        self.dl_connector = dl_connector
