from typing import Any, Dict, cast, List

from pydantic import BaseModel

from ..types import ColumnDef, ColumnSort, ITable, TableData, TData, TFeatureFactory, Updater, update_state


class ColumnState(BaseModel):
    column_name: str
    reverse: bool = False


class DefaultColumnSort(ColumnSort[TData]):

    def __init__(self, table: ITable[TData], updater: Updater[TData], state: Dict[str, ColumnState]):
        super().__init__(table, updater)
        self._all_columns_state = state
        self._active_column_state: ColumnState | None = None


    @update_state
    def toggle_sort(self, col: ColumnDef) -> bool:
        self._active_column_state = self.get_state(col, toggle=True)
        return self._active_column_state.reverse


    def is_sort_reverse(self, col: ColumnDef) -> bool:
        state = self.get_state(col)
        return state.reverse


    def get_state(self, col: ColumnDef, toggle:bool=False) -> ColumnState:
        state = self._all_columns_state[col.name]
        state.reverse ^= toggle
        return state


    def pipeline(self, table_data:TableData[TData]) -> TableData[TData]:

        def _sort(col: ColumnState, row: Any):
            """use the column name to return the row column value"""
            return getattr(row, col.column_name)

        if self._active_column_state is not None:
            col = self._active_column_state
            rows = cast(List[TData], table_data.rows.sort(key=lambda element: _sort(col, element), reverse=col.reverse))
            return TableData(rows=rows, cols=table_data.cols)
        else:
            return table_data


def getDefaultColumnSort() -> TFeatureFactory[TData, ColumnSort[TData]]:

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> ColumnSort[TData]:
        state: Dict[str, ColumnState] = {}
        for col in table.data.cols:
            name = col if isinstance(col, str) else col.name
            state[name] = ColumnState(column_name=col.name)
        return DefaultColumnSort(table=table, updater=updater, state=state)

    return wrapper
