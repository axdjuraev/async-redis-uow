from typing import Generic, List, Optional
from .types import TIModel, TOModel
from .all_getter import AllGetterRepo


class PaginatedAllGetterRepo(AllGetterRepo[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def page(self, filters: str = '', count: Optional[int] = None, page: Optional[int] = None) -> List[TOModel]:
        objs = await self.all(filters)

        if count and page:
            return objs[(count or 1) * page - count:count]

        return objs
