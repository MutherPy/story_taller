from fastapi import FastAPI

from providers.plugs.infrastructure_plugs import sql_db_provider, sql_db_uow_provider

from providers.implementations.infrastructure_impl import get_sql_db_session, get_sql_db_uow_provider


def _bind_infra_providers(app: FastAPI) -> None:
    app.dependency_overrides[sql_db_provider] = get_sql_db_session
    app.dependency_overrides[sql_db_uow_provider] = get_sql_db_uow_provider


def bind_providers(app: FastAPI) -> None:
    _bind_infra_providers(app=app)
