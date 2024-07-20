from api.controllers.enter_exit.router import auth_router
from fastapi import Depends
from providers.plugs.infrastructure_plugs import sql_db_uow_provider


@auth_router.get('/login')
async def login(uow=Depends(sql_db_uow_provider)):
    print(uow)
    from uuid_extensions import uuid7str
    print((await uow.user_q_rep.retrieve(uuid7str())))
    return 'hello'
