from typing import Callable, Generic, List, Protocol

from ..types import (
    Columns,
    ColumnSort,
    SortState,
    SortCallback,
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


class IPaginationOptions(Protocol, Generic[TData]):
    manual_pagination: bool = False
    on_pagination_change: PaginatorCallback | None = None
    page_count: int | None = None
    pagination: bool = False
    paginator: TFeatureFactory[TData, Paginator[TData]] |None = None


class ISortOptions(Protocol, Generic[TData]):
    sorter: TFeatureFactory[TData, ColumnSort[TData]] | None = None

    sorting: SortState | None = None
    manual_sorting: bool = False
    on_sort_change: SortCallback | None = None
    sort: bool = True


class ISearchOptions(Protocol, Generic[TData]):
    search: TFeatureFactory[TData, TableSearch[TData]] | None = None


class IRowModelOptions(Protocol, Generic[TData]):
    row_model: TFeatureFactory[TData, RowModel[TData]] | None = None


class Options(TableData[TData],
              IPaginationOptions[TData],
              ISortOptions[TData],
              ISearchOptions[TData],
              IRowModelOptions[TData],
              ITableState[TData],
              Generic[TData]):

    def __init__(
        self,
        rows: List[TData],
        cols: Columns,

        # Paginator

        manual_pagination: bool = False,
        on_pagination_change: PaginatorCallback | None = None,
        page_count: int | None = None,
        pagination: bool = False,
        paginator: TFeatureFactory[TData, Paginator[TData]] | None = None,

        # Sort

        manual_sorting: bool  = False,
        on_sort_change: SortCallback | None = None,
        sorter: TFeatureFactory[TData, ColumnSort[TData]] | None = None,
        sorting: SortState | None = None,
        sort: bool = True,

        # Row model

        row_model: TFeatureFactory[TData, RowModel[TData]] | None = None,

        # Search

        search: TFeatureFactory[TData, TableSearch[TData]] | None = None
    ):
        super().__init__(rows=rows, cols=cols)

        # Pagination

        self.manual_pagination = manual_pagination
        self.on_pagination_change = on_pagination_change
        self.page_count = page_count
        self.pagination = pagination
        self.paginator = paginator

        # Sort

        self.sorter = sorter
        self.manual_sorting = manual_sorting
        self.on_sort_change = on_sort_change
        self.sorting = sorting

        # Row model

        self.row_model = row_model

        # Search

        self.search = search
