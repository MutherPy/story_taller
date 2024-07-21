from api.controllers.enter_exit.router import auth_router
from fastapi import Depends


@auth_router.post('/login')
async def login():
    return 'hello'
