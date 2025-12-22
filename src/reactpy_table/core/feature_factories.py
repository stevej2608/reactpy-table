from dataclasses import dataclass
from typing import Generic

from ..types import ColumnSort, Paginator, RowModel, TableSearch, TData, TFeatureFactory


@dataclass
class FeatureFactories(Generic[TData]):
    paginator: TFeatureFactory[TData, Paginator[TData]]
    sort: TFeatureFactory[TData, ColumnSort[TData]]
    search: TFeatureFactory[TData, TableSearch[TData]]
    row_model: TFeatureFactory[TData, RowModel[TData]]
