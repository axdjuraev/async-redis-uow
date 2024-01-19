from typing import Generic
from .types import TIModel, TOModel
from .base import BaseRepoCreator
from redis.commands.json.path import Path


class BaseSetterRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def set_base(self, obj: dict):
        self.session.json().set(self.hname, Path('$').strPath, obj)
        return obj

