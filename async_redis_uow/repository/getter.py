from typing import Generic, Union
from .types import TIModel, TOModel
from .base import BaseRepoCreator
from redis.commands.json.path import Path
from redis.exceptions import ResponseError


class GetterRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def get(self, id, filters: str = '') -> Union[TOModel, None]: 
        try: 
            obj = await self.session.json().get(
                self.hname, 
                Path(f'.{id}{filters}').strPath,
            ).execute()  # type: ignore
        except ResponseError as e:
            return print(str(e))

        return obj and self.OSchema(**obj[-1])

