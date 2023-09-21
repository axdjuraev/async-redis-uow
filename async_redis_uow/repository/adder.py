import json
from typing import Generic
from .types import TIModel, TOModel
from .base import BaseRepoCreator
from redis.commands.json.path import Path


class AdderRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def add(self, obj: TIModel):
        id = self.get_obj_id(obj)
        self.session.json().set(
            self.hname, 
            Path(f'$.{id}').strPath,
            json.loads(obj.json()),
        )
        return obj

