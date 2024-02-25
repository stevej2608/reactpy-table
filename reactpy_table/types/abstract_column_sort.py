from typing import Protocol

from .abstract_table import TData
from .feature import FeatureBase, IFeature
from .table_data import Column


class IColumnSort(IFeature[TData], Protocol):
    def toggle_sort(self, col: Column) -> bool:
        ...

    def is_sort_reverse(self, col: Column) -> bool:
        ...


class ColumnSort(IColumnSort[TData], FeatureBase[TData]):
    pass
