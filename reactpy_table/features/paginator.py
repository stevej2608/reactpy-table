from typing import Tuple, Any
from ctypes import ArgumentError
import math

from utils.logger import log
from utils.memo import memo, TMemo

from ..types import ITable, Paginator, TableData, TData, TFeatureFactory, Updater, update_state


DEFAULT_PAGE_SIZE = 10


class DefaultPaginator(Paginator[TData]):

    def __init__(self, table: ITable[TData], updater: Updater[TData], page_size: int):
        super().__init__(table, updater)
        self._page_size = page_size
        self._page_index = 0

        self.pipeline = memo(
            self.get_deps,
            self.expensive_computation,
            {'onChange': self.on_change}
            )


    def get_deps(self) -> Tuple[int, int]:
        return (1, 2)

    def expensive_computation(self, a: int, b: int) -> int:
        print("Performing expensive computation...")
        return a + b

    def on_change(self, result: int):
        print(f"Result changed: {result}")


    # def pipeline(self) -> TMemo:
    #     return memo(self.get_deps, self.expensive_computation, {'onChange': self.on_change})


    @property
    def page_index(self) -> int:
        return self._page_index

    @property
    def page_size(self) -> int:
        return self._page_size

    @property
    def page_base(self) -> int:
        return self.page_size * self.page_index + 1

    @property
    def page_count(self) -> int:
        row_count = len(self._pipeline_data.rows)
        return math.ceil(row_count / self.page_size)

    @property
    def row_count(self) -> int:
        return len(self._pipeline_data.rows)

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

        self._page_index = int((self.page_index * self.page_size) / page_size)
        self._page_size = page_size

    @update_state
    def set_page_index(self, page_index: int):
        if page_index < 0 or page_index > self.page_count-1:
            raise ArgumentError(f'Requested page {page_index} is not in range [0..{self.page_count-1}]')
        self._page_index = page_index


    def can_get_previous_page(self) -> bool:
        return self.page_index > 0

    def can_get_next_page(self) -> bool:
        page_count = self.page_count
        return self.page_index < page_count - 1


    # def pipeline(self, table_data:TableData[TData]) -> TableData[TData]:

    #     if self._pipeline_data != table_data:

    #         self._pipeline_data = table_data

    #         low = self.page_size * self.page_index
    #         high = min(low + self.page_size, len(self._pipeline_data.rows))

    #         rows = self._pipeline_data.rows[low:high]
    #         table_data = TableData(rows=rows, cols=table_data.cols)

    #     return  table_data



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
