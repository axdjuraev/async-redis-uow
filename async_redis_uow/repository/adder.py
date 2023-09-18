from uuid import uuid4
from typing import Generic
from .types import TIModel, TOModel
from .base import BaseRepoCreator


class AdderRepo(BaseRepoCreator[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True

    async def add(self, obj: TIModel):
        id = _ if hasattr(obj, 'id') and (_ := getattr(obj, 'id')) else str(uuid4())
        return self.session.hset(
            self.hname, 
            id, 
            self.dumps(obj.dict()),
        )

    async def get(self, *identifiers):
        return await super().get(*identifiers)

