from typing import Callable, Generic, List, Protocol

from ..types import (
    Columns,
    ColumnSort,
    SortCallback,
    ITable,
    Paginator,
    PaginatorCallback,
    RowModel,
    TableData,
    TableSearch,
    SearchCallback,
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
    pagination_feature: TFeatureFactory[TData, Paginator[TData]] |None = None


class ISortOptions(Protocol, Generic[TData]):
    sort_feature: TFeatureFactory[TData, ColumnSort[TData]] | None = None
    manual_sorting: bool = False
    on_sort_change: SortCallback | None = None
    sort: bool = True


class ISearchOptions(Protocol, Generic[TData]):
    search_feature: TFeatureFactory[TData, TableSearch[TData]] | None = None
    manual_search: bool = False
    on_search_change: SearchCallback | None = None
    search: bool = True


class IRowModelOptions(Protocol, Generic[TData]):
    row_model_feature: TFeatureFactory[TData, RowModel[TData]] | None = None


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
        pagination_feature: TFeatureFactory[TData, Paginator[TData]] | None = None,

        # Sort

        manual_sorting: bool  = False,
        on_sort_change: SortCallback | None = None,
        sort_feature: TFeatureFactory[TData, ColumnSort[TData]] | None = None,
        sort: bool = True,

        # Row model

        row_model_feature: TFeatureFactory[TData, RowModel[TData]] | None = None,

        # Search

        search_feature: TFeatureFactory[TData, TableSearch[TData]] | None = None,
        manual_search: bool  = False,
        on_search_change: SearchCallback | None = None,
        search: bool = True,
    ):
        super().__init__(rows=rows, cols=cols)

        # Pagination

        self.manual_pagination = manual_pagination
        self.on_pagination_change = on_pagination_change
        self.page_count = page_count
        self.pagination = pagination
        self.pagination_feature = pagination_feature

        # Sort

        self.sort_feature = sort_feature
        self.manual_sorting = manual_sorting
        self.on_sort_change = on_sort_change

        # Row model

        self.row_model_feature = row_model_feature

        # Search

        self.search_feature = search_feature
        self.manual_search = manual_search
        self.on_search_change = on_search_change
        self.search = search
