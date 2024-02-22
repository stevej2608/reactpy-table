from typing import Protocol

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable

class ITableSearch(IFeature, Protocol):

    @staticmethod
    def init(table: ITable, updater:Updater) -> 'ITableSearch':
        raise NotImplementedError()

    def table_search(self, text:str): ...


class TableSearch(ITableSearch, FeatureBase):

    @staticmethod
    def init(table: ITable, updater:Updater) -> ITableSearch:
        raise NotImplementedError()
