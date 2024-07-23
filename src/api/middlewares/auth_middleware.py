from http import HTTPStatus

from starlette.requests import HTTPConnection
from starlette.responses import Response
from starlette.types import ASGIApp, Receive, Scope, Send

from infrastructure.services.auth.id_provider import IdentityProvider


class AuthMiddleware:
    def __init__(self, app: ASGIApp, public_paths: list[str], tst) -> None:
        self.app = app
        self.public_paths = ['/docs', '/openapi.json']
        self.public_paths.extend(public_paths)

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope['type'] not in ['http', 'websocket']:
            r = Response(status_code=HTTPStatus.IM_A_TEAPOT)
            await r(scope, receive, send)
            return

        conn = HTTPConnection(scope)

        if self.public_paths:
            if '*' in self.public_paths:
                await self.app(scope, receive, send)
                return
            for p_path in self.public_paths:
                if p_path in conn.url.path:
                    await self.app(scope, receive, send)
                    return

        token = conn.headers.get('Authorization')

        if not token or not IdentityProvider.validate_token(token):
            r = Response(status_code=HTTPStatus.UNAUTHORIZED)
            await r(scope, receive, send)
            return

        await self.app(scope, receive, send)
