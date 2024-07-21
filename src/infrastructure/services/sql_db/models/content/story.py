from sqlalchemy import ForeignKey

from infrastructure.services.sql_db.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from uuid_extensions import uuid7str

from infrastructure.services.sql_db.models.many_to_many.story_tags import story_to_tags_association_table


class Story(BaseModel):
    __tablename__ = 'story'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7str)

    author_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))

    title: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)

    tags = relationship(
        "Tag",
        secondary=story_to_tags_association_table,
        back_populates="stories"
    )
