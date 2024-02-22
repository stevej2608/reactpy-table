from ..types import RowModel, Updater, ITable, TRowModel


class DefaultRowModel(RowModel[TRowModel]):

    @staticmethod
    def init(table: ITable[TRowModel], updater:Updater[TRowModel]) -> RowModel[TRowModel]:
        return DefaultRowModel(table=table, updater=updater)
