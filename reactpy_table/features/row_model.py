from typing import Tuple, Any, List
from enum import Enum
from ctypes import ArgumentError
from pydantic import BaseModel
from utils.memo import memo, MemoOpts
from ..types import ITable, RowModel, TData, TableData, TFeatureFactory, UpstreamData, update_state

class Action(Enum):
    DELETE = 1
    UPDATE = 2

class RowAction(BaseModel):
    action: Action | None = None
    index: int = -1
    row: Any | None = None

NO_ACTION = RowAction()


class DefaultRowModel(RowModel[TData]):

    def __init__(self, table: ITable[TData], upstream_data: UpstreamData[TData]):
        super().__init__(table, upstream_data)

        self.row_actions: List[RowAction[TData]] = []

        def deps() -> Tuple[TableData[TData], List[RowAction]]:
            return (
                upstream_data(),
                self.row_actions.copy()
            )

        def updater(upstream_data: TableData[TData], row_actions:List[RowAction]) -> TableData[TData]:

            if not row_actions:
                return upstream_data

            rows = upstream_data.rows.copy()

            for action in row_actions:

                if action.action == Action.DELETE:
                    del rows[action.index]

                if action.action == Action.UPDATE and action.row:
                    rows[action.index] = action.row

            return TableData(rows=rows, cols=upstream_data.cols)


        self.pipeline = memo(deps, updater, MemoOpts(name='  1. DefaultRowModel', debug=True))


    def table_index(self, index:int) -> int:
        """Check range and return index as range[0..n]

        Args:
            index (int): user index [1...n] 

        Raises:
            ArgumentError: Exception if index is out of range

        Returns:
            int: table index [0..n]
        """

        if index < 1 or index > len(self.table.data.rows):
            raise ArgumentError('Table index is out of range')
        return index - 1

    @update_state
    def delete_row(self, index:int) -> None:
        index=self.table_index(index)
        self.row_actions.append(RowAction(action=Action.DELETE,index=index))


    @update_state
    def update_row(self, index:int, row:TData) -> None:
        index=self.table_index(index)
        self.row_actions.append(RowAction(action=Action.UPDATE,index=index, row=row))


def getDefaultRowModel() -> TFeatureFactory[TData, RowModel[TData]]:

    def wrapper(table: ITable[TData], upstream_data: UpstreamData[TData]) -> RowModel[TData]:
        return DefaultRowModel(table=table, upstream_data=upstream_data)

    return wrapper
