from typing import Callable, Generic, List

from ..types import (
    Columns,
    ColumnSort,
    ITable,
    Paginator,
    PaginatorCallback,
    RowModel,
    TableData,
    TableSearch,
    TData,
    TFeatureFactory,
    UpstreamData,
)

from .core_options import ITableState

PaginatorType = Callable[[ITable[TData], UpstreamData[TData]], Paginator[TData]] | None
ColumnSortType = Callable[[ITable[TData], UpstreamData[TData]], ColumnSort[TData]] | None
TableSearchType = Callable[[ITable[TData], UpstreamData[TData]], TableSearch[TData]] | None


class Options(TableData[TData], ITableState[TData], Generic[TData]):
    paginator: TFeatureFactory[TData, Paginator[TData]] |None = None
    row_model: TFeatureFactory[TData, RowModel[TData]] | None = None
    sort: TFeatureFactory[TData, ColumnSort[TData]] | None = None
    search: TFeatureFactory[TData, TableSearch[TData]] | None = None

    pagination: bool = False
    manual_pagination: bool = False
    on_pagination_change: PaginatorCallback | None = None
    page_count: int | None = None

    def __init__(
        self,
        rows: List[TData],
        cols: Columns,

        pagination: bool = False,
        manual_pagination: bool = False,
        page_count: int | None = None,

        paginator: TFeatureFactory[TData, Paginator[TData]] | None = None,
        on_pagination_change: PaginatorCallback | None = None,
        row_model: TFeatureFactory[TData, RowModel[TData]] | None = None,
        sort: TFeatureFactory[TData, ColumnSort[TData]] | None = None,
        search: TFeatureFactory[TData, TableSearch[TData]] | None = None
    ):
        super().__init__(rows=rows, cols=cols)

        self.paginator = paginator
        self.manual_pagination = manual_pagination
        self.page_count = page_count
        self.on_pagination_change = on_pagination_change
        self.row_model = row_model
        self.sort = sort
        self.search = search
        self.pagination = pagination

