from fastapi import FastAPI

from providers.plugs.infrastructure_plugs import (
    sql_db_provider,
    sql_db_uow_provider,
    main_uow_provider
)
from providers.plugs.facades.auth import auth_facade_provider


from providers.implementations.infrastructure_impl import (
    get_sql_db_provider,
    get_sql_db_uow_provider,
    get_main_uow_provider
)
from providers.implementations.facades.auth import get_auth_facade_provider

def _bind_infra_providers(app: FastAPI) -> None:
    app.dependency_overrides[sql_db_provider] = get_sql_db_provider
    app.dependency_overrides[sql_db_uow_provider] = get_sql_db_uow_provider
    app.dependency_overrides[main_uow_provider] = get_main_uow_provider


def _bind_facades(app: FastAPI) -> None:
    app.dependency_overrides[auth_facade_provider] = get_auth_facade_provider


def bind_providers(app: FastAPI) -> None:
    _bind_infra_providers(app=app)
    _bind_facades(app=app)
