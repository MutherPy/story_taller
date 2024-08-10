from sqlalchemy import Table, Column, ForeignKey, Integer

from infrastructure.services.sql_db.models.base_model import metadata


permission_to_group_association_table = Table(
    "permission_to_group_association_table",
    metadata,
    Column("permission_id", Integer(), ForeignKey("permission.id"), primary_key=True),
    Column("permission_group_id", Integer(), ForeignKey("permission_group.id"), primary_key=True),
)
