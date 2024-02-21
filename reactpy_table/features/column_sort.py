from typing import Dict, Any
from pydantic import BaseModel

from ..types.abstract_column_sort import IColumnSort
from ..types import Column, ITable, Updater

from .feature_base import FeatureBase, update_state

class ColumnState(BaseModel):
    reverse: bool = False


class DefaultColumnSort(IColumnSort, FeatureBase):

    state: Dict[str, ColumnState]

    @staticmethod
    def init(table: ITable, updater:Updater) -> "DefaultColumnSort":

        state: Dict[str, ColumnState] = {}
        for col in table.data.cols:
            name = col if isinstance(col, str) else col.name
            state[name] = ColumnState()

        return DefaultColumnSort(table, updater, state=state)


    def __init__(self, table: ITable, updater:Updater, state:Dict[str, ColumnState]):
        super().__init__(table, updater)
        self.state = state


    @update_state
    def toggle_sort(self, col:Column) -> bool:

        def _sort(col:Column, element: Any):
            name = col if isinstance(col, str) else col.name
            return getattr(element, name)

        state = self.get_state(col)
        state.reverse = not state.reverse

        self.data.rows.sort(key=lambda element: _sort(col, element), reverse=state.reverse)

        return state.reverse


    def is_sort_reverse(self, col:Column)-> bool:
        state = self.get_state(col)
        return state.reverse


    def get_state(self, col:Column):
        return self.state[col.name]
