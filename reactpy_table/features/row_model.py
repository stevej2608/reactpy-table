from ..types import RowModel, Updater, ITable, TData, TCommonFeature


class DefaultRowModel(RowModel[TData]):
    ...


def getDefaultRowModel() -> TCommonFeature[TData, RowModel[TData]]:

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> RowModel[TData]:
        return DefaultRowModel(table=table, updater=updater)

    return wrapper
