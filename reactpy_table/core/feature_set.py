from dataclasses import dataclass
from typing import Type, Protocol, Generic

from ..types import IColumnSort, IPaginator,IRowModel, ITableSearch
from ..types import ColumnSort, Paginator, RowModel, TableSearch, TData

@dataclass
class Features(Generic[TData]):
    paginator: Type[Paginator[TData]]
    sort: Type[ColumnSort[TData]]
    search: Type[TableSearch[TData]]
    row_model: Type[RowModel[TData]]


class IFeatureSet(Protocol, Generic[TData]):
    paginator: IPaginator[TData]
    sort: IColumnSort[TData]
    search: ITableSearch[TData]
    row_model: IRowModel[TData]
