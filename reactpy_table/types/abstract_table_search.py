from typing import Protocol

from .feature import IFeature, Updater
from .abstract_table import ITable

class ITableSearch(IFeature, Protocol):

    @staticmethod
    def init(table: ITable, updater:Updater) -> 'ITableSearch':
        raise NotImplementedError()

    def table_search(self, text:str): ...
