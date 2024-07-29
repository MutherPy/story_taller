from infrastructure.services.sql_db.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.services.sql_db.models.many_to_many.stories_tags import story_to_tags_association_table
from infrastructure.services.sql_db.models.many_to_many.users_tags import users_to_tags_association_table


class TagDB(BaseModel):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(unique=True)

    stories = relationship(
        "StoryDB",
        secondary=story_to_tags_association_table,
        back_populates="tags"
    )

    users = relationship(
        "UserDB",
        secondary=users_to_tags_association_table,
        back_populates="tags"
    )
