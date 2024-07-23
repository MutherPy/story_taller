from interfaces.infrastructure.repositories.command.user import IUserCommandRepository
from interfaces.infrastructure.repositories.query.user import IUserQueryRepository
from interfaces.infrastructure.uow import IBaseCommonUOW
from abc import ABC


class IDBUoW(IBaseCommonUOW, ABC):
    user_q_rep: IUserQueryRepository
    user_c_rep: IUserCommandRepository
