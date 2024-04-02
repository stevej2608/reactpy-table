import logging
from typing import List, Tuple

from pydantic import BaseModel
from reactpy import use_effect, use_memo, use_state

from reactpy_table.types.paginator_state import PaginatorState
from reactpy_table.types.search_state import SearchState
from reactpy_table.types.sort_state import SortState
from utils import DT

from ..books.db import Book, BookDatabase

log = logging.getLogger(__name__)

class DBQuery(BaseModel):
    sort: SortState
    pagination: PaginatorState
    search: SearchState

    def __str__(self):
        return f"sort({self.sort}), pagination({self.pagination}), search({self.search})"


BookList = List[Book]
EMPTY_BOOK_LIST: BookList = []

# https://reactpy.dev/docs/reference/hooks-api.html#async-effects

def use_api(url:str, query:DBQuery) -> Tuple[BookList, int, bool]:

    db = use_memo(lambda: BookDatabase(url=url),[url])

    data, set_data = use_state(EMPTY_BOOK_LIST)
    page_count, set_page_count = use_state(0)
    loading, set_loading = use_state(False)

    def _get_data():

        dt = DT()

        set_loading(True)

        skip = query.pagination.page_size * query.pagination.page_index
        limit = query.pagination.page_size

        col = query.sort.id
        desc = query.sort.desc

        search_term = query.search.search_term

        table_data, row_count = db.get_books(search_term, skip, limit, col, desc)

        log.info("fetched %d books in %s ms", len(table_data), dt())

        set_data(table_data)
        set_page_count(int(row_count / limit))

        set_loading(False)

    use_effect(_get_data, [url, str(query)])


    return (data, page_count, loading)
