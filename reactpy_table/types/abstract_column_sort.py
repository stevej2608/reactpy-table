from typing import Protocol

from .abstract_table import TData
from .feature import FeatureBase, IFeature
from .table_data import ColumnDef


class IColumnSort(IFeature[TData], Protocol):
    def toggle_sort(self, col: ColumnDef) -> bool:
        ...

    def is_sort_reverse(self, col: ColumnDef) -> bool:
        ...


class ColumnSort(IColumnSort[TData], FeatureBase[TData]):
    pass
