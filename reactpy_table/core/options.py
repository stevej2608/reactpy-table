from typing import Callable, Generic, List, Protocol
from ..features.feature_control import FeatureControl

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
    pagination_feature: TFeatureFactory[TData, Paginator[TData]] |None
    on_pagination_change: PaginatorCallback | None
    pagination_control: FeatureControl
    page_count: int | None


class ISortOptions(Protocol, Generic[TData]):
    sort_feature: TFeatureFactory[TData, ColumnSort[TData]] | None
    on_sort_change: SortCallback | None
    sort_control: FeatureControl



class ISearchOptions(Protocol, Generic[TData]):
    search_feature: TFeatureFactory[TData, TableSearch[TData]] | None
    on_search_change: SearchCallback | None
    search_control: FeatureControl



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

        pagination_feature: TFeatureFactory[TData, Paginator[TData]] | None = None,
        on_pagination_change: PaginatorCallback | None = None,
        pagination_control: FeatureControl = FeatureControl.DISABLED,
        page_count: int | None = None,

        # Sort

        on_sort_change: SortCallback | None = None,
        sort_feature: TFeatureFactory[TData, ColumnSort[TData]] | None = None,
        sort_control: FeatureControl  = FeatureControl.DEFAULT,

        # Row model

        row_model_feature: TFeatureFactory[TData, RowModel[TData]] | None = None,

        # Search

        search_feature: TFeatureFactory[TData, TableSearch[TData]] | None = None,
        on_search_change: SearchCallback | None = None,
        search_control: FeatureControl  = FeatureControl.DEFAULT,

    ):
        super().__init__(rows=rows, cols=cols)

        # Pagination

        self.pagination_feature = pagination_feature
        self.on_pagination_change = on_pagination_change
        self.pagination_control = pagination_control
        self.page_count = page_count

        # Sort

        self.sort_feature = sort_feature
        self.on_sort_change = on_sort_change
        self.sort_control = sort_control

        # Row model

        self.row_model_feature = row_model_feature

        # Search

        self.search_feature = search_feature
        self.on_search_change = on_search_change
        self.search_control = search_control

