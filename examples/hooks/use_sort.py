import logging
from typing import Tuple

from reactpy import use_state

from reactpy_table.types.sort_state import SortCallback, SortState, SQL_DIRECTION

log = logging.getLogger(__name__)

def use_sorting(initial_field:str = "id", initial_order:SQL_DIRECTION = "ASC") -> Tuple[SortState, SortCallback]:

    sorting, set_sorting = use_state(SortState(id=initial_field, desc=initial_order))

    def _set_sorting(state: SortState) -> None:
        log.info('set_sort(state=%s)', state)
        set_sorting(state)


    return (sorting, _set_sorting)
