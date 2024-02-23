from typing import Protocol
from .table_data import Column

from .feature import IFeature, FeatureBase
from .abstract_table import TData


class IColumnSort(IFeature[TData], Protocol):
    def toggle_sort(self, col: Column) -> bool:
        ...

    def is_sort_reverse(self, col: Column) -> bool:
        ...


class ColumnSort(IColumnSort[TData], FeatureBase[TData]):
    pass
