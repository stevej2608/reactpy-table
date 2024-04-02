import logging
from typing import Tuple

from reactpy import use_state

from reactpy_table.types.search_state import SearchCallback, SearchState


log = logging.getLogger(__name__)


def use_search() -> Tuple[SearchState, SearchCallback]:

    search, set_search = use_state(SearchState())

    def _set_search(state: SearchState) -> None:
        log.info('set_search(state=%s)', state)
        set_search(state)


    return (search, _set_search)
