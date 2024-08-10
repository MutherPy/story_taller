from infrastructure.services.sql_db.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.services.sql_db.models.many_to_many.permissions_groups import permission_to_group_association_table


class PermissionGroupDB(BaseModel):
    __tablename__ = 'permission_group'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(nullable=True)

    permissions = relationship(
        "PermissionDB",
        secondary=permission_to_group_association_table,
        lazy="selectin"
    )
