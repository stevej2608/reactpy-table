from typing import Generic, Protocol, Self

from .abstract_column_sort import IColumnSort
from .abstract_paginator import IPaginator
from .abstract_row_model import IRowModel
from .abstract_table import ITable
from .abstract_table_search import ITableSearch
from .table_state import TableState, TData


class IFeatureSet(Generic[TData], Protocol):
    paginator: IPaginator[TData]
    sort: IColumnSort[TData]
    search: ITableSearch[TData]
    row_model: IRowModel[TData]


class Table(ITable[TData], IFeatureSet[TData], Protocol):
    """External view of the table seen by users & features"""

    def refresh(self) -> Self:
        ...


    def set_options(self, table_options: TableState[TData]) -> None:
        ...

    @property
    def UID(self) -> int:
        ...
