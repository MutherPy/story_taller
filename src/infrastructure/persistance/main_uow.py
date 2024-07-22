
from infrastructure.persistance.bases.uow import BaseMainUOW
from infrastructure.services.sql_db.uow import DbUOW
from interfaces.infrastructure.main_uow import IMainUOW


class MainUOW(BaseMainUOW, IMainUOW):
    db: DbUOW

