from infrastructure.services.sql_db.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from uuid_extensions import uuid7str


class User(BaseModel):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7str)

    name: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)

    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    stories = relationship("Story")
