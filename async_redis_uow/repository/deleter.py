from typing import Generic
from .types import TIModel, TOModel
from .base import BaseRepoCreator
from redis.commands.json.path import Path


class DeleterRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def delete(self, id):
        return self.session.json().delete(
            self.hname,
            Path(f'$.{id}').strPath,
        )

