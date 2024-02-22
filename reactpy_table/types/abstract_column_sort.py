from typing import Protocol
from .table_data import Column

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable, TRowModel

class IColumnSort(IFeature[TRowModel], Protocol):

    @staticmethod
    def init(table: ITable[TRowModel], updater:Updater[TRowModel]) -> 'IColumnSort[TRowModel]':
        raise NotImplementedError()

    def toggle_sort(self, col:Column) -> bool: ...

    def is_sort_reverse(self, col:Column) -> bool: ...


class ColumnSort(IColumnSort[TRowModel], FeatureBase[TRowModel]):

    @staticmethod
    def init(table: ITable[TRowModel], updater:Updater[TRowModel]) -> IColumnSort[TRowModel]:
        raise NotImplementedError()
