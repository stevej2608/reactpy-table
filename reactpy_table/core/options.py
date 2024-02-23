from typing import Generic, List, Type

from ..types import Columns, ColumnSort, Paginator, TableData, TableSearch, TData

type FeatureType[T] = Type[T] | None

class Options(TableData[TData], Generic[TData]):

    paginator: FeatureType[Paginator[TData]] = None
    sort: FeatureType[ColumnSort[TData]] = None
    search: FeatureType[TableSearch[TData]] = None

    def __init__(self,
            rows: List[TData],
            cols: Columns,
            paginator: FeatureType[Paginator[TData]] = None,
            sort: FeatureType[ColumnSort[TData]] = None,
            search: FeatureType[TableSearch[TData]] = None
            ):

        super().__init__(rows=rows, cols=cols)

        self.paginator = paginator
        self.sort = sort
        self.search = search
