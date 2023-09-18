from typing import Type, Generic
from axabc.db.async_repository import AbstractAsyncRepository
from 
from .types import TIModel, TOModel


class BaseRepoCreator(AbstractAsyncRepository, Generic[TIModel, TOModel]):
    Schema: Type[TIModel]
    OSchema: Type[TOModel]

    __abstract__ = False

    def __init__(self, session: ) -> None:
        super().__init__(session)

