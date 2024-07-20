from infrastructure.services.sql_db.db import AsyncDBProxy


db_proxy_for_provider: AsyncDBProxy = AsyncDBProxy.initialize()



