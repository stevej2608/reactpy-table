from ..types import RowModel, Updater, ITable


class DefaultRowModel(RowModel):

    @staticmethod
    def init(table: ITable, updater:Updater) -> RowModel:
        return DefaultRowModel(table=table, updater=updater)
