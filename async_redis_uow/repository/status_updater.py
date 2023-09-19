from typing import Generic
from redis.commands.json.path import Path
from .types import TIModel, TOModel
from .base import BaseRepoCreator


class StatusUpdaterRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def deactivate(self, id):
        return self.update_status(id, status=False)

    async def update_status(self, id, status: bool): 
        return self.session.json().set(
            self.hname, 
            Path(f'$.{id}.is_active').strPath,
            status,
        )

