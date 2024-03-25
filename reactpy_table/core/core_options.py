from typing import Protocol, Generic, List, cast, Any

from ..types.paginator_state import PaginatorCallback
from ..types.table_data import TData, Columns

class ICoreTableOptions(Protocol, Generic[TData]):
    pagination: bool
    manual_pagination: bool
    on_pagination_change: PaginatorCallback | None
    page_count: int | None

    rows: List[TData]
    cols: Columns


class CoreTableOptions(ICoreTableOptions[TData], Generic[TData]):

    def __init__(self, options: ICoreTableOptions[TData]):
        self.pagination = options.pagination
        self.manual_pagination = options.manual_pagination
        self.on_pagination_change = options.on_pagination_change
        self.page_count = options.page_count
        self.rows = options.rows
        self.cols = options.cols


    def __eq__(self, value: object) -> bool:

        if not isinstance(value, CoreTableOptions):
            return False

        val: CoreTableOptions[TData] = cast(CoreTableOptions[TData], value)

        if self.pagination != val.pagination:
            return False

        if self.manual_pagination != val.manual_pagination:
            return False

        # if self.on_pagination_change != value.on_pagination_change:
        #     return False

        if self.page_count != val.page_count:
            return False

        if self.rows != val.rows:
            return False

        if self.cols != val.cols:
            return False

        return True


    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value=value)

