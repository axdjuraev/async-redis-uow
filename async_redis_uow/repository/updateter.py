import json
from typing import Generic
from .types import TIModel, TOModel
from .base import BaseRepoCreator
from redis.commands.json.path import Path


class UpdateterRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def update(self, obj: TIModel):
        id = self.get_obj_id(obj)
        return self.session.json().set(
            self.hname, 
            Path(f'$.{id}').strPath,
            json.loads(obj.json()),
        )

