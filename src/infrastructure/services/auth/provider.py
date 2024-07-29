from typing import Optional

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends

from application.dto.auth.auth import AuthUserDTO, TokenDataDTO

from infrastructure.services.auth.id_provider import IdentityProvider

from providers.plugs.infrastructure_common_plugs import sql_db_uow_provider

sec = HTTPBearer(auto_error=False)


async def get_current_user(creds: HTTPAuthorizationCredentials = Depends(sec), db_uow=Depends(sql_db_uow_provider)) -> Optional[AuthUserDTO]:
    token_data: TokenDataDTO = IdentityProvider.validate_token(creds.credentials)
    auth_user_dto: Optional[AuthUserDTO] = await db_uow.user_q_rep.retrieve_id_by_username(username=token_data.username)
    return auth_user_dto



