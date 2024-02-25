import math
from typing import Any, List

from utils.logger import log

from ..types import ITable, Paginator, TData, TFeatureFactory, Updater, update_state

DEFAULT_PAGE_SIZE = 10


class DefaultPaginator(Paginator[TData]):

    def __init__(self, table: ITable[TData], updater: Updater[TData], page_size: int):
        super().__init__(table, updater)
        self.page_size = page_size

    @property
    def rows(self) -> List[Any]:
        low = self.page_size * self.page_index
        high = min(low + self.page_size, len(self.data.rows))
        return self.data.rows[low:high]

    @property
    def page_count(self) -> int:
        row_count = len(self.data.rows)
        return math.ceil(row_count / self.page_size)

    @property
    def row_count(self) -> int:
        return len(self.data.rows)

    def first_page(self):
        self.set_page_index(0)

    def previous_page(self):
        if self.page_index > 0:
            self.set_page_index(self.page_index - 1)

    def next_page(self):
        if self.page_index < self.page_count - 1:
            self.set_page_index(self.page_index + 1)

    def last_page(self):
        last_page = self.page_count - 1
        self.set_page_index(last_page)

    @update_state
    def set_page_size(self, page_size: int):
        log.info("set_page_size")

        self.page_index = int((self.page_index * self.page_size) / page_size)
        self.page_size = page_size

    @update_state
    def set_page_index(self, page_index: int):
        self.page_index = page_index

    def can_get_previous_page(self) -> bool:
        return self.page_index > 0

    def can_get_next_page(self) -> bool:
        page_count = self.page_count

        # if page_count == -1:
        #     return True

        # if page_count == 0:
        #     return False

        return self.page_index < page_count - 1


def getDefaultPaginator(page_size: int=DEFAULT_PAGE_SIZE) -> TFeatureFactory[TData, Paginator[TData]]:
    """Return a wrapped function that when called creates a DefaultPaginator instance

    Args:
        page_size (int, optional): The default page size. Defaults to DEFAULT_PAGE_SIZE.

    Returns:
        Callable[[ITable[TData], Updater[TData]], Paginator[TData]]: A function that creates the default paginator
    """

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> Paginator[TData]:
        return DefaultPaginator(table=table, updater=updater, page_size=page_size)

    return wrapper
