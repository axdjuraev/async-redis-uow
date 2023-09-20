from typing import Generic
from .types import TIModel, TOModel
from .base import BaseRepoCreator
from redis.commands.json.path import Path


class GetterRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def get(self, id, filters: str = '') -> TOModel:
        obj = await self.session.json().get(
            self.hname, 
            Path(f'.{id}{filters}').strPath,
        ).execute()  # type: ignore

        return obj and self.OSchema(**obj[-1])

