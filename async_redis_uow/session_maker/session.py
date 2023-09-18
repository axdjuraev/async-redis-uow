from typing import Protocol, runtime_checkable
from redis.asyncio.client import Pipeline


@runtime_checkable
class ExecuteAbleQuery(Protocol):
    async def execute(self):
        raise NotImplementedError


class LazySession(Pipeline):
    async def execute(self):
        return await super().execute()

    async def commit(self):
        return await super().execute()

    async def rollback(self):
        return await super().discard()

    async def close(self):
        return await self.__aexit__(None, None, None)

