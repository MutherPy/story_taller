import enum
from typing import TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import InstrumentedAttribute


AlchemyTable = TypeVar('AlchemyTable')


class BaseFilter(BaseModel):
    def db_filter_clause(self, table_cls: AlchemyTable) -> list:
        self_dict: dict = self.model_dump(exclude_none=True)
        result = []
        for field, value in self_dict.items():
            table_cls_field = getattr(table_cls, field, None)
            if isinstance(table_cls_field, InstrumentedAttribute):
                if isinstance(getattr(self, field), enum.Enum):
                    result.append(table_cls_field == value)
                else:
                    if not isinstance(value, list):
                        result.append(table_cls_field.like(f'%{value}%'))

        return result

    def db_filter_in(self, table_cls: AlchemyTable, rename=None) -> list:
        if rename is None:
            rename = {}

        self_dict: dict = self.model_dump(exclude_none=True)
        result = []
        for field, value in self_dict.items():
            if field in rename.keys():
                field = rename[field]

            table_cls_field = getattr(table_cls, field, None)
            if isinstance(table_cls_field, InstrumentedAttribute):
                if isinstance(value, list):
                    if len(value) > 0:
                        result.append(table_cls_field.in_(value))
        return result

    def db_filter_int_in(self, table_cls: AlchemyTable, rename=None) -> list:
        if rename is None:
            rename = {}

        self_dict: dict = self.model_dump(exclude_none=True)
        result = []
        for field, value in self_dict.items():
            if field in rename.keys():
                field = rename[field]

            if not value:
                continue

            if isinstance(value, str):
                value = value.split(',')
                try:
                    value = list(map(int, value))
                except Exception:
                    continue

            table_cls_field = getattr(table_cls, field, None)
            if isinstance(table_cls_field, InstrumentedAttribute):
                if isinstance(value, list):
                    if len(value) > 0:
                        result.append(table_cls_field.in_(value))
        return result

    def db_filter_in_range(self, table_cls: AlchemyTable, db_field_name: str) -> list:
        self_dict: dict = self.model_dump(exclude_none=True)
        result = []
        for field, value in self_dict.items():
            table_cls_field = getattr(table_cls, db_field_name, None)
            if isinstance(table_cls_field, InstrumentedAttribute):
                if field == 'range_from':
                    result.append(table_cls_field >= value)
                if field == 'range_to':
                    result.append(table_cls_field <= value)

        return result
