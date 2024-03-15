from typing import Tuple
from ctypes import ArgumentError
from utils.memo import memo
from ..types import ITable, RowModel, TData, TableData, EMPTY_TABLE, TFeatureFactory, Updater, update_state

class DefaultRowModel(RowModel[TData]):

    def __init__(self, table: ITable[TData], updater: Updater[TData]):
        super().__init__(table, updater)

        self.pipeline = memo(
            self.get_deps,
            self.expensive_computation,
            {'onChange': self.on_change}
            )


    def get_deps(self) -> Tuple[int, int]:
        return (1, 2)

    def expensive_computation(self, a: int, b: int) -> TableData[TData]:
        return EMPTY_TABLE

    def on_change(self, result: int):
        print(f"Result changed: {result}")


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
        index = self.table_index(index)
        del self.table.data.rows[index]


    @update_state
    def update_row(self, index:int, row:TData) -> None:
        index = self.table_index(index)
        self.table.data.rows[index] = row


    # def pipeline(self, table_data:TableData[TData]) -> TableData[TData]:
    #     return table_data


def getDefaultRowModel() -> TFeatureFactory[TData, RowModel[TData]]:

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> RowModel[TData]:
        return DefaultRowModel(table=table, updater=updater)

    return wrapper
