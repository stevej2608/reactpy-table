from typing import Dict, Any, Callable
from pydantic import BaseModel

from ..types import Column, ITable, Updater, ColumnSort, update_state, TData


class ColumnState(BaseModel):
    reverse: bool = False


class DefaultColumnSort(ColumnSort[TData]):
    state: Dict[str, ColumnState]

    def __init__(self, table: ITable[TData], updater: Updater[TData], state: Dict[str, ColumnState]):
        super().__init__(table, updater)
        self.state = state

    @update_state
    def toggle_sort(self, col: Column) -> bool:
        def _sort(col: Column, element: Any):
            name = col if isinstance(col, str) else col.name
            return getattr(element, name)

        state = self.get_state(col)
        state.reverse = not state.reverse

        self.data.rows.sort(key=lambda element: _sort(col, element), reverse=state.reverse)

        return state.reverse

    def is_sort_reverse(self, col: Column) -> bool:
        state = self.get_state(col)
        return state.reverse

    def get_state(self, col: Column):
        return self.state[col.name]


def getDefaultColumnSort() -> Callable[[ITable[TData], Updater[TData]], ColumnSort[TData]]:

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> ColumnSort[TData]:
        state: Dict[str, ColumnState] = {}
        for col in table.data.cols:
            name = col if isinstance(col, str) else col.name
            state[name] = ColumnState()
        return DefaultColumnSort(table=table, updater=updater, state=state)

    return wrapper
