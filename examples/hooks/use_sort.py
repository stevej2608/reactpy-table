from typing import Tuple

from reactpy import use_state

from reactpy_table.types.sort_state import SortCallback, SortState, SQL_DIRECTION
from utils import log


# export function useSorting(initialField = "id", initialOrder = "ASC") {
#   const [sorting, setSorting] = useState([
#     { id: initialField, desc: initialOrder === "DESC" },
#   ]);

#   return {
#     sorting,
#     onSortingChange: setSorting,
#     order: !sorting.length ? initialOrder : sorting[0].desc ? "DESC" : "ASC",
#     field: sorting.length ? sorting[0].id : initialField,
#   };
# }


def use_sorting(initial_field:str = "id", initial_order:SQL_DIRECTION = "ASC") -> Tuple[SortState, SortCallback]:

    sorting, set_sorting = use_state(SortState(id=initial_field, desc=initial_order))

    def _set_sorting(state: SortState) -> None:
        log.info('set_sort(state=%s)', state)
        set_sorting(state)


    return (sorting, _set_sorting)
