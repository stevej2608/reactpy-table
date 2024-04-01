from typing import Protocol, Generic, List, cast

# from reactpy_table.types import search_state

from ..types.paginator_state import PaginatorCallback
from ..types.sort_state import SortState, SortCallback
from ..types.search_state import SearchState, SearchCallback

from ..types.table_data import TData, Columns

class ITableState(Protocol, Generic[TData]):
    rows: List[TData]
    cols: Columns

    # Pagination

    pagination: bool
    manual_pagination: bool
    on_pagination_change: PaginatorCallback | None
    page_count: int | None

    # Sort

    sorting: SortState | None = None
    manual_sorting: bool = False
    on_sort_change: SortCallback | None = None
    sort: bool = False

    # Search

    manual_search: bool = False
    on_search_change: SearchCallback | None = None



class TableState(ITableState[TData], Generic[TData]):

    def __init__(self, options: ITableState[TData]):
        self.rows = options.rows
        self.cols = options.cols

        # Pagination

        self.pagination = options.pagination
        self.manual_pagination = options.manual_pagination
        self.on_pagination_change = options.on_pagination_change
        self.page_count = options.page_count

        # Sort

        self.sorting = options.sorting
        self.manual_sorting = options.manual_sorting
        self.on_sort_change  = options.on_sort_change
        self.sort = options.sort

        # Search

        self.manual_search = options.manual_search
        self.on_search_change = options.on_search_change


    def __eq__(self, value: object) -> bool:

        if not isinstance(value, TableState):
            return False

        val: TableState[TData] = cast(TableState[TData], value)

        if self.rows != val.rows:
            return False

        if self.cols != val.cols:
            return False

        # Pagination

        if self.pagination != val.pagination:
            return False

        if self.manual_pagination != val.manual_pagination:
            return False

        if self.page_count != val.page_count:
            return False

        # Sort

        if self.sorting != val.sorting:
            return False

        if self.manual_sorting != val.manual_sorting:
            return False

        if self.sort != val.sort:
            return False


        return True


    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value=value)
