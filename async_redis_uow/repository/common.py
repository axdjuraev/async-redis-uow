from typing import Generic
from .types import TIModel, TOModel
from .adder import AdderRepo
from .getter import GetterRepo
from .updateter import UpdateterRepo
from .deleter import DeleterRepo
from .paginated import PaginatedRepo
from .status_updater import StatusUpdaterRepo
from .paginated_all_getter import PaginatedAllGetterRepo


class BaseRepository(
    AdderRepo[TIModel, TOModel], 
    GetterRepo[TIModel, TOModel], 
    UpdateterRepo[TIModel, TOModel], 
    DeleterRepo[TIModel, TOModel],
    PaginatedRepo[TIModel, TOModel],
    StatusUpdaterRepo[TIModel, TOModel],
    PaginatedAllGetterRepo[TIModel, TOModel],
    Generic[TIModel, TOModel],
):
    __abstract__ = True

