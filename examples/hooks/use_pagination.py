import logging
from typing import Tuple

from reactpy import use_state

from reactpy_table.types.paginator_state import PaginatorCallback, PaginatorState


log = logging.getLogger(__name__)


def use_pagination(initial_size: int = 10) -> Tuple[PaginatorState, PaginatorCallback]:
    pagination, set_pagination = use_state(PaginatorState(page_index=0, page_size=initial_size))

    def _set_page(state: PaginatorState) -> None:
        log.info('set_page(state=%s)', state)
        set_pagination(state)


    return (pagination, _set_page)
