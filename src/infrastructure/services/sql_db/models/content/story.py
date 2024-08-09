from datetime import datetime

from sqlalchemy import ForeignKey

from infrastructure.services.sql_db.choices.story import StoryStatus
from infrastructure.services.sql_db.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from uuid_extensions import uuid7str
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import Enum as Alchemy_enum

from infrastructure.services.sql_db.models.many_to_many.stories_tags import story_to_tags_association_table


class StoryDB(BaseModel):
    __tablename__ = 'story'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7str)

    author_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    author = relationship("UserDB", back_populates="stories", lazy="selectin")

    title: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)

    tags = relationship(
        "TagDB",
        secondary=story_to_tags_association_table,
        back_populates="stories",
        lazy="selectin"
    )

    status: Mapped[StoryStatus] = mapped_column(
        Alchemy_enum(StoryStatus),
        server_default="DRAFT",
        nullable=False
    )

    creation_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
