from typing import Protocol, runtime_checkable
from redis.asyncio.client import Pipeline
from axabc.db.session_mapper import LazySession as _LazySession


@runtime_checkable
class ExecuteAbleQuery(Protocol):
    async def execute(self):
        raise NotImplementedError


class LazySession(_LazySession, Pipeline):
    async def execute(self, query: ExecuteAbleQuery):
        return await query.execute()

    async def commit(self):
        return self.save()

    async def rollback(self):
        return await super().discard()

    async def close(self):
        return await self.__aexit__(None, None, None)

