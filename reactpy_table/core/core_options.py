from typing import Protocol, Generic, List, cast

# from reactpy_table.types import search_state

from ..types.paginator_state import PaginatorCallback
from ..types.sort_state import SortState, SortCallback
from ..types.search_state import SearchCallback

from ..types.table_data import TData, Columns
from ..features.feature_control import FeatureControl

class ITableState(Protocol, Generic[TData]):
    rows: List[TData]
    cols: Columns

    # Pagination

    pagination_control: FeatureControl
    on_pagination_change: PaginatorCallback | None
    page_count: int | None

    # Sort

    sort_control: FeatureControl
    on_sort_change: SortCallback | None

    # Search

    search_control: FeatureControl
    on_search_change: SearchCallback | None



class TableState(ITableState[TData], Generic[TData]):

    def __init__(self, options: ITableState[TData]):
        self.rows = options.rows
        self.cols = options.cols

        # Pagination

        self.pagination_control = options.pagination_control
        self.on_pagination_change = options.on_pagination_change
        self.page_count = options.page_count

        # Sort

        self.sort_control = options.sort_control
        self.on_sort_change  = options.on_sort_change

        # Search

        self.search_control = options.search_control
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

        if self.pagination_control != val.pagination_control:
            return False


        if self.page_count != val.page_count:
            return False

        # Sort

        if self.sort_control != val.sort_control:
            return False


        return True


    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value=value)
