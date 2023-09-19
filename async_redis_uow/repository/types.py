from typing import TypeVar
from axabc.db import BaseSchema


TIModel = TypeVar("TIModel", bound=BaseSchema)
TOModel = TypeVar("TOModel", bound=BaseSchema)

