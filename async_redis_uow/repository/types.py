from typing import TypeVar
from async_redis_uow.schemas import BaseModel


TIModel = TypeVar("TIModel", bound=BaseModel)
TOModel = TypeVar("TOModel", bound=BaseModel)

