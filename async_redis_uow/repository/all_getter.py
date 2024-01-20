from typing import Any, Callable, Generic, List, Optional
from pydantic import parse_obj_as
from redis.commands.json.path import Path
from redis.exceptions import ResponseError
from .types import TIModel, TOModel
from .base import BaseRepoCreator


class AllGetterRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    def _all_sort_key(self, obj: TOModel):
        return obj.created_at

    async def all(
        self, 
        filters: Optional[str] = None, 
        *, 
        parse: bool = True, 
        sort_func: Optional[Callable[[TOModel], Any]] = None,
    ) -> List[TOModel]:
        filters = filters or '$.[*]'

        try:
            objs = await self.session.json().get(
                self.hname, 
                Path(f'{filters}').strPath,
            ).execute()  # type: ignore
        except ResponseError:
            return []
        
        objs = self._unwrap_till(objs)

        if parse:
            sort_func = sort_func or self._all_sort_key
            return sorted(parse_obj_as(List[self.OSchema], objs), key=sort_func)
        
        return objs

