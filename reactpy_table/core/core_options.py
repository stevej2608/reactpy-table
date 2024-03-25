from pickle import FALSE
from typing import Protocol, Self
from pydantic import BaseModel

from ..types.paginator_state import PaginatorCallback

class ICoreTableOptions(Protocol):
    pagination: bool = False
    manual_pagination: bool = False
    on_pagination_change: PaginatorCallback | None = None
    page_count: int | None = None


class CoreTableOptions(BaseModel):
    pagination: bool = False
    manual_pagination: bool = False
    on_pagination_change: PaginatorCallback | None = None
    page_count: int | None = None

    def __init__(self, options: ICoreTableOptions):
        super().__init__(
            pagination = options.pagination,
            manual_pagination = options.manual_pagination,
            on_pagination_change = options.on_pagination_change,
            page_count = options.page_count
        )


    def __eq__(self, value: object) -> bool:

        if not isinstance(value, CoreTableOptions):
            return False

        if self.pagination != value.pagination:
            return False

        if self.manual_pagination != value.manual_pagination:
            return False

        # if self.on_pagination_change != value.on_pagination_change:
        #     return False

        if self.page_count != value.page_count:
            return False

        return True


    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value=value)
