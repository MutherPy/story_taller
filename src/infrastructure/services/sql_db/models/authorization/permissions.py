from infrastructure.services.sql_db.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.services.sql_db.models.many_to_many.permissions_groups import permission_to_group_association_table


class PermissionDB(BaseModel):
    __tablename__ = 'permission'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[str] = mapped_column(nullable=False)

    groups = relationship(
        "PermissionGroupDB",
        secondary=permission_to_group_association_table,
        lazy="selectin"
    )

