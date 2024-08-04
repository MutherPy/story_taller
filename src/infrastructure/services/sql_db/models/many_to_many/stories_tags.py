from sqlalchemy import Table, Column, ForeignKey, UUID, Integer

from infrastructure.services.sql_db.models.base_model import metadata


story_to_tags_association_table = Table(
    "story_to_tags_association_table",
    metadata,
    Column("tag_id", Integer(), ForeignKey("tag.id"), primary_key=True),
    Column("story_id", UUID(), ForeignKey("story.id"), primary_key=True),
)
