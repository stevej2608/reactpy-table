from typing import Protocol

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable, TData

class ITableSearch(IFeature[TData], Protocol):

    def table_search(self, search_term:str, case_sensitive:bool=False): ...


class TableSearch(ITableSearch[TData], FeatureBase[TData]):

    @staticmethod
    def init(table: ITable[TData], updater:Updater[TData]) -> ITableSearch[TData]:
        raise NotImplementedError()
