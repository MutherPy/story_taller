
from infrastructure.persistance.bases.uow import BaseMainUOW
from infrastructure.services.sql_db.uow import DbUOW


class MainUOW(BaseMainUOW):
    db: DbUOW

