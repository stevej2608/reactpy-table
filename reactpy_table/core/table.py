from typing import Generic, Protocol

from ..types import IColumnSort, IPaginator, IRowModel, ITable, ITableSearch, TData


class IFeatureSet(Generic[TData], Protocol):
    paginator: IPaginator[TData]
    sort: IColumnSort[TData]
    search: ITableSearch[TData]
    row_model: IRowModel[TData]


class Table(ITable[TData], IFeatureSet[TData], Protocol):
    ...
