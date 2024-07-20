from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, registry
from sqlalchemy.ext.asyncio import AsyncAttrs


metadata = MetaData()
mapper_registry = registry(metadata=metadata)


class BaseModel(AsyncAttrs, DeclarativeBase):
    registry = mapper_registry
    metadata = mapper_registry.metadata
