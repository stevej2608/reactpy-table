from typing import Protocol

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable, TData

class IRowModel(IFeature[TData], Protocol):
    pass


class RowModel(IRowModel[TData], FeatureBase[TData]):

    @staticmethod
    def init(table: ITable[TData], updater:Updater[TData]) -> IRowModel[TData]:
        raise NotImplementedError()
