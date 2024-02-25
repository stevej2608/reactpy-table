from typing import Generic, List, Callable

from ..types import Columns, ColumnSort, Paginator, TableData, TableSearch, TData, ITable, Updater, TCommonFeature


PaginatorType = Callable[[ITable[TData], Updater[TData]], Paginator[TData]] | None
ColumnSortType = Callable[[ITable[TData], Updater[TData]], ColumnSort[TData]] | None
TableSearchType = Callable[[ITable[TData], Updater[TData]], TableSearch[TData]] | None



class Options(TableData[TData], Generic[TData]):
    paginator: TCommonFeature[TData, Paginator[TData]] | None = None
    sort: TCommonFeature[TData, ColumnSort[TData]] | None = None
    search: TCommonFeature[TData, TableSearch[TData]] | None = None

    def __init__(
        self,
        rows: List[TData],
        cols: Columns,
        paginator: TCommonFeature[TData, Paginator[TData]] | None = None,
        sort: TCommonFeature[TData, ColumnSort[TData]] | None = None,
        search: TCommonFeature[TData, TableSearch[TData]] | None = None,
    ):
        super().__init__(rows=rows, cols=cols)

        self.paginator = paginator
        self.sort = sort
        self.search = search
