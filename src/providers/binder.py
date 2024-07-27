from fastapi import FastAPI

from providers.plugs.infrastructure_common_plugs import (
    sql_db_provider,
    sql_db_uow_provider,
)
from providers.plugs.main_providers_plugs import main_uow_provider


from providers.implementations.infrastructure_common_impl import (
    get_sql_db_provider,
    get_sql_db_uow_provider,
)
from providers.implementations.main_providers_impl import get_main_uow_provider


def _bind_infra_common_providers(app: FastAPI) -> None:
    app.dependency_overrides[sql_db_provider] = get_sql_db_provider
    app.dependency_overrides[sql_db_uow_provider] = get_sql_db_uow_provider


def _bind_main_providers(app: FastAPI) -> None:
    app.dependency_overrides[main_uow_provider] = get_main_uow_provider


def bind_providers(app: FastAPI) -> None:
    _bind_infra_common_providers(app=app)
    _bind_main_providers(app=app)
