from typing import Generic, Protocol, Self

from ..types import IColumnSort, IPaginator, IRowModel, ITable, ITableSearch, TData

from .core_options import TableState

class IFeatureSet(Generic[TData], Protocol):
    paginator: IPaginator[TData]
    sort: IColumnSort[TData]
    search: ITableSearch[TData]
    row_model: IRowModel[TData]


class Table(ITable[TData], IFeatureSet[TData], Protocol):

    def refresh(self) -> Self:
        ...

    def set_options(self, table_options: TableState[TData]) -> None:
        ...

    @property
    def UID(self) -> int:
        ...
