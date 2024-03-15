from typing import Tuple
from ctypes import ArgumentError
from utils.memo import memo, MemoOpts
from ..types import ITable, RowModel, TData, TableData, TFeatureFactory, UpstreamData, update_state

class DefaultRowModel(RowModel[TData]):

    def __init__(self, table: ITable[TData], upstream_data: UpstreamData[TData]):
        super().__init__(table, upstream_data)

        def deps() -> Tuple[TableData[TData]]:
            return (upstream_data(),)

        def updater(upstream_data: TableData[TData]) -> TableData[TData]:
            return upstream_data

        self.pipeline = memo(deps, updater, MemoOpts(name='4. DefaultRowModel'))


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


def getDefaultRowModel() -> TFeatureFactory[TData, RowModel[TData]]:

    def wrapper(table: ITable[TData], upstream_data: UpstreamData[TData]) -> RowModel[TData]:
        return DefaultRowModel(table=table, upstream_data=upstream_data)

    return wrapper
