from typing import Callable, Generic, List

from ..types import Columns, ColumnSort, ITable, Paginator, TableData, TableSearch, RowModel, TData, TFeatureFactory, UpstreamData

PaginatorType = Callable[[ITable[TData], UpstreamData[TData]], Paginator[TData]] | None
ColumnSortType = Callable[[ITable[TData], UpstreamData[TData]], ColumnSort[TData]] | None
TableSearchType = Callable[[ITable[TData], UpstreamData[TData]], TableSearch[TData]] | None


class Options(TableData[TData], Generic[TData]):
    paginator: TFeatureFactory[TData, Paginator[TData]] | None = None
    row_model: TFeatureFactory[TData, RowModel[TData]] | None = None
    sort: TFeatureFactory[TData, ColumnSort[TData]] | None = None
    search: TFeatureFactory[TData, TableSearch[TData]] | None = None

    def __init__(
        self,
        rows: List[TData],
        cols: Columns,
        paginator: TFeatureFactory[TData, Paginator[TData]] | None = None,
        row_model: TFeatureFactory[TData, RowModel[TData]] | None = None,
        sort: TFeatureFactory[TData, ColumnSort[TData]] | None = None,
        search: TFeatureFactory[TData, TableSearch[TData]] | None = None
    ):
        super().__init__(rows=rows, cols=cols)

        self.paginator = paginator
        self.row_model = row_model
        self.sort = sort
        self.search = search
