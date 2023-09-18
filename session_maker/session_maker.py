from typing import Optional
from redis.asyncio.client import Redis
from axabc.db.session_mapper import LazySessionMaker as _LazySessionMaker

from .session import LazySession


class RedisLazySessionMaker(_LazySessionMaker, Redis):
    def __call__(self, transaction: bool = True, shard_hint: Optional[str] = None) -> LazySession:
        return LazySession(self.connection_pool, self.response_callbacks, transaction, shard_hint)  # type: ignore

