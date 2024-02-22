from typing import Protocol
from .table_data import Column

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable

class IColumnSort(IFeature, Protocol):

    @staticmethod
    def init(table: ITable, updater:Updater) -> 'IColumnSort':
        raise NotImplementedError()

    def toggle_sort(self, col:Column) -> bool: ...

    def is_sort_reverse(self, col:Column) -> bool: ...


class ColumnSort(IColumnSort, FeatureBase):

    @staticmethod
    def init(table: ITable, updater:Updater) -> IColumnSort:
        raise NotImplementedError()
