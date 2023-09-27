from typing import Generic, Iterable, Optional
from axsqlalchemy.repository.paginated import math
from redis.commands.json.path import Path
from .types import TIModel, TOModel
from .all_getter import AllGetterRepo


class PaginatedRepo(AllGetterRepo[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def all_page_count(self, filters: str = '', count: Optional[int] = None) -> int:
        all_count = await self.all_count(filters)
        return math.ceil(all_count / count) if count else 1 

    async def all_count(self, filters: str = ''):
        res = await self.session.json().objlen(
            self.hname, 
            Path(f'${filters}').strPath,
        ).execute()  # type: ignore

        return res[-1][-1] if res and res[-1] and isinstance(res[-1], Iterable) else 0

