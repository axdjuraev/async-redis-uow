from typing import TypeVar
from pydantic import BaseModel


TIModel = TypeVar("TIModel", bound=BaseModel)
TOModel = TypeVar("TOModel", bound=BaseModel)

