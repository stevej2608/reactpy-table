
from typing import List, Any
import math
from utils.logger import log
from ..types import Paginator, Updater, ITable, update_state

DEFAULT_PAGE_SIZE = 10


class DefaultPaginator(Paginator):

    @staticmethod
    def init(table: ITable, updater:Updater) -> Paginator:
        return DefaultPaginator(table=table, updater=updater, page_size=DEFAULT_PAGE_SIZE)


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
    def row_count(self) -> int :
        return len(self.data.rows)


    def __init__(self, table: ITable, updater:Updater, page_size:int):
        super().__init__(table, updater)
        self.page_size = page_size


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
    def set_page_size(self, page_size:int):
        log.info('set_page_size')

        self.page_index = int((self.page_index * self.page_size) /  page_size)
        self.page_size = page_size


    @update_state
    def set_page_index(self, page_index:int):
        self.page_index = page_index


    def can_get_previous_page(self) -> bool:
        return self.page_index > 0


    def can_get_next_page(self) -> bool:
        page_count = self.page_count

        if page_count == -1:
            return True

        if page_count == 0:
            return False

        return self.page_index < page_count - 1
