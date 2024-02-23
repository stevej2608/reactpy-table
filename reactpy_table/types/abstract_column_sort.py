from typing import Protocol
from .table_data import Column

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable, TData


class IColumnSort(IFeature[TData], Protocol):
    def toggle_sort(self, col: Column) -> bool:
        ...

    def is_sort_reverse(self, col: Column) -> bool:
        ...


class ColumnSort(IColumnSort[TData], FeatureBase[TData]):
    @staticmethod
    def init(table: ITable[TData], updater: Updater[TData]) -> IColumnSort[TData]:
        raise NotImplementedError()
