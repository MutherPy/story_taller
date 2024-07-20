import api.controllers.enter_exit.login
import api.controllers.enter_exit.logout
import api.controllers.enter_exit.registration

from api.controllers.enter_exit.router import auth_router

__all__ = [
    'auth_router',
]