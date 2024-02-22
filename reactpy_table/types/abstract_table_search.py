from typing import Protocol

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable, TRowModel

class ITableSearch(IFeature[TRowModel], Protocol):

    @staticmethod
    def init(table: ITable[TRowModel], updater:Updater[TRowModel]) -> 'ITableSearch[TRowModel]':
        raise NotImplementedError()

    def table_search(self, search_term:str, case_sensitive:bool=False): ...


class TableSearch(ITableSearch[TRowModel], FeatureBase[TRowModel]):

    @staticmethod
    def init(table: ITable[TRowModel], updater:Updater[TRowModel]) -> ITableSearch[TRowModel]:
        raise NotImplementedError()
