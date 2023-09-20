
from typing import Generic, List
from pydantic import parse_obj_as
from redis.commands.json.path import Path
from .types import TIModel, TOModel
from .base import BaseRepoCreator


class AllGetterRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def all(self, filters: str = ''):
        objs = await self.session.json().get(
            self.hname, 
            Path(f'$.[*]{filters}').strPath,
        ).execute()  # type: ignore

        return parse_obj_as(List[self.OSchema], objs[-1])

