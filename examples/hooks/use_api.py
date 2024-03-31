from typing import Tuple, List
from pydantic import BaseModel

from reactpy import use_state, use_effect, use_memo

from reactpy_table.types.sort_state import SortState
from reactpy_table.types.paginator_state import PaginatorState

from  ..books.db2 import Book, BookDatabase

from utils import log, DT

class DBQuery(BaseModel):
    sort: SortState
    pagination: PaginatorState

    def __str__(self):
        return f"sort({self.sort}, pagination({self.pagination}))"


BookList = List[Book]
EMPTY_BOOK_LIST: BookList = []

# https://reactpy.dev/docs/reference/hooks-api.html#async-effects

def use_api(url:str, query:DBQuery) -> Tuple[BookList, int, bool]:

    db = use_memo(lambda: BookDatabase(url=url),[url])

    data, set_data = use_state(EMPTY_BOOK_LIST)
    count, set_count = use_state(0)
    loading, set_loading = use_state(False)

    def _get_data():

        dt = DT()

        set_loading(True)

        skip = query.pagination.page_size * query.pagination.page_index
        limit = query.pagination.page_size

        col = query.sort.id
        desc = query.sort.desc

        table_data, page_count = db.get_books("", skip, limit, col, desc)

        log.info("fetched %d books in %s ms", len(table_data), dt())

        set_data(table_data)
        set_count(page_count)

        set_loading(False)

    use_effect(_get_data, [url, str(query)])


    return (data, count, loading)
