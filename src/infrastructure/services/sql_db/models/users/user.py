from infrastructure.services.sql_db.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from uuid_extensions import uuid7str

from infrastructure.services.sql_db.models.many_to_many.users_tags import users_to_tags_association_table


class UserDB(BaseModel):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7str)

    name: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    stories = relationship("StoryDB", back_populates='author')

    tags = relationship(
        "TagDB",
        secondary=users_to_tags_association_table,
        back_populates="users",
        lazy="selectin"  # https://stackoverflow.com/questions/74252768/missinggreenlet-greenlet-spawn-has-not-been-called
    )
