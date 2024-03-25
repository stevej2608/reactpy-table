from typing import Dict, Tuple, Any

from pydantic import BaseModel
from utils.memo import memo, MemoOpts

from ..types import ColumnDef, ColumnSort, ITable, TData, TableData, TFeatureFactory, UpstreamData, update_state


class ColumnState(BaseModel):
    column_name: str
    reverse: bool = False

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"ColumnState[{id(self)}](column_name={self.column_name}, reverse={self.reverse})"


class DefaultColumnSort(ColumnSort[TData]):

    def __init__(self, table: ITable[TData], upstream_data: UpstreamData[TData], state: Dict[str, ColumnState]):
        super().__init__(table, upstream_data)
        self._all_columns_state = state
        self._active_column_state: ColumnState | None = None


        def deps() -> Tuple[TableData[TData], ColumnState | None]:
            return (
                upstream_data(),
                self._active_column_state.model_copy() if self._active_column_state else None
            )

        def updater(upstream_data: TableData[TData],
                   active_column_state: ColumnState | None
                   ) -> TableData[TData]:

            table_data = upstream_data

            # log.info('active_column_state=%s', active_column_state)

            def _sort(col: ColumnState, row: Any):
                """use the column name to return the row column value"""
                return getattr(row, col.column_name)

            if active_column_state is not None  and active_column_state.reverse:
                col = active_column_state
                rows = table_data.rows.copy()
                rows.sort(key=lambda element: _sort(col, element), reverse=True)
                return TableData(rows=rows, cols=table_data.cols)
            else:
                return table_data

        self.pipeline = memo(deps, updater, MemoOpts(name='      3. DefaultColumnSort', debug=True))


    @update_state
    def toggle_sort(self, col: ColumnDef) -> bool:
        self._active_column_state = self.get_state(col, toggle=True)
        return self._active_column_state.reverse


    def is_sort_reverse(self, col: ColumnDef) -> bool:
        state = self.get_state(col)
        return state.reverse


    def get_state(self, col: ColumnDef, toggle:bool=False) -> ColumnState:
        state = self._all_columns_state[col.name]
        if toggle:
            state.reverse = not state.reverse
        return state

def getDefaultColumnSort() -> TFeatureFactory[TData, ColumnSort[TData]]:

    def wrapper(table: ITable[TData], updater: UpstreamData[TData]) -> ColumnSort[TData]:
        state: Dict[str, ColumnState] = {}
        for col in table.data.cols:
            name = col if isinstance(col, str) else col.name
            state[name] = ColumnState(column_name=col.name)
        return DefaultColumnSort(table=table, upstream_data=updater, state=state)

    return wrapper
