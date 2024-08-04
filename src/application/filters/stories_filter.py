from application.bases.base_filter import BaseFilter
from fastapi import Query
from pydantic import Field, field_validator, ValidationError


class StoriesTagsListFilter(BaseFilter):
    tags_ids: str = Field(Query(''))
