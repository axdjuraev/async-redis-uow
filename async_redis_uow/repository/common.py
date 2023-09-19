from typing import Generic
from .types import TIModel, TOModel
from .adder import AdderRepo
from .getter import GetterRepo


class BaseRepository(AdderRepo[TIModel, TOModel], GetterRepo[TIModel, TOModel], Generic[TIModel, TOModel]):
    __abstract__ = True


