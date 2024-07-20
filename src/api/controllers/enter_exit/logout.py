from api.controllers.enter_exit.router import auth_router


@auth_router.post('/logout')
async def logout():
    ...
