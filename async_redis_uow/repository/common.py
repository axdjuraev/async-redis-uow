from typing import Generic
from .types import TIModel, TOModel
from .adder import AdderRepo
from .getter import GetterRepo
from .updateter import UpdateterRepo
from .deleter import DeleterRepo


class BaseRepository(
    AdderRepo[TIModel, TOModel], 
    GetterRepo[TIModel, TOModel], 
    UpdateterRepo[TIModel, TOModel], 
    Generic[TIModel, TOModel],
    DeleterRepo[TIModel, TOModel],
):
    __abstract__ = True


