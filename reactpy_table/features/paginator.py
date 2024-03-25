from typing import Tuple
from ctypes import ArgumentError
import math

from utils.logger import log
from utils.memo import memo, MemoOpts

from ..types import ITable, Paginator, PaginatorState, TableData, TData, TFeatureFactory, UpstreamData

from .null_updater import null_updater


DEFAULT_PAGE_SIZE = 10


class DefaultPaginator(Paginator[TData]):

    def __init__(self, table: ITable[TData], upstream_data: UpstreamData[TData], page_size: int):
        super().__init__(table, upstream_data)
        self.upstream_data = upstream_data
        self._paginator_state = PaginatorState(page_index=0, page_size=page_size)


        def deps() -> Tuple[TableData[TData], int, int, bool]:
            return (
                upstream_data(),
                self.page_size,
                self.page_index,
                self.table.table_options.pagination
            )

        def updater(upstream_data: TableData[TData],
                   page_size: int,
                   page_index:int,
                   enabled: bool
                   ) -> TableData[TData]:

            if not enabled:
                return upstream_data

            low = page_size * page_index
            high = min(low + page_size, len(upstream_data.rows))

            rows = upstream_data.rows[low:high]
            table_data = TableData(rows=rows, cols=upstream_data.cols)
            return table_data


        if self.table.table_options.manual_pagination:
            self.pipeline = null_updater(upstream_data=upstream_data)
        elif self.table.table_options.pagination:
            self.pipeline = memo(deps, updater, MemoOpts(name='    2. DefaultPaginator', debug=True))
        else:
            ...


    @property
    def page_index(self) -> int:
        return self._paginator_state.page_index

    @property
    def page_size(self) -> int:
        return self._paginator_state.page_size

    @property
    def page_base(self) -> int:
        return self.page_size * self.page_index + 1

    @property
    def page_count(self) -> int:
        pages = self.table.table_options.page_count
        if pages is None:
            pages = math.ceil(self.row_count / self.page_size)
        return pages

    @property
    def row_count(self) -> int:
        return len(self.upstream_data().rows)

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


    def set_page_size(self, page_size: int):
        log.info("set_page_size")
        self.set_pagination(self.page_index, page_size)


    def set_page_index(self, page_index: int):
        if page_index < 0 or page_index > self.page_count-1:
            raise ArgumentError(f'Requested page {page_index} is not in range [0..{self.page_count-1}]')
        self.set_pagination(page_index, self.page_size)


    # @update_state
    def set_pagination(self, page_index: int, page_size: int):

        page_index = int((page_index * page_size) / page_size)
        new_state = PaginatorState(page_index=page_index, page_size=page_size)

        if new_state != self._paginator_state:

            self._paginator_state = new_state

            if self.table.table_options.on_pagination_change:
                log.info('>>>>>>>>>> Refresh')
                self.table.table_options.on_pagination_change(new_state)

            self.refresh()


    def can_get_previous_page(self) -> bool:
        return self.page_index > 0

    def can_get_next_page(self) -> bool:
        page_count = self.page_count
        return self.page_index < page_count - 1


def getDefaultPaginator(page_size: int=DEFAULT_PAGE_SIZE) -> TFeatureFactory[TData, Paginator[TData]]:
    """Return a wrapped function that when called creates a DefaultPaginator instance

    Args:
        page_size (int, optional): The default page size. Defaults to DEFAULT_PAGE_SIZE.

    Returns:
        Callable[[ITable[TData], Updater[TData]], Paginator[TData]]: A function that creates the default paginator
    """

    def wrapper(table: ITable[TData], upstream_data: UpstreamData[TData]) -> Paginator[TData]:
        return DefaultPaginator(table, upstream_data, page_size=page_size)

    return wrapper
