from typing import Callable
from ..types import RowModel, Updater, ITable, TData


class DefaultRowModel(RowModel[TData]):
    ...


def getDefaultRowModel() -> Callable[[ITable[TData], Updater[TData]], RowModel[TData]]:

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> RowModel[TData]:
        return DefaultRowModel(table=table, updater=updater)

    return wrapper
