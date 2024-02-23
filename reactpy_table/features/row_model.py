from ..types import RowModel, Updater, ITable, TData


class DefaultRowModel(RowModel[TData]):
    @staticmethod
    def init(table: ITable[TData], updater: Updater[TData]) -> RowModel[TData]:
        return DefaultRowModel(table=table, updater=updater)
