from sqlalchemy import Table, Column, ForeignKey

from infrastructure.services.sql_db.models.base_model import metadata


users_to_tags_association_table = Table(
    "users_to_tags_association_table",
    metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)
