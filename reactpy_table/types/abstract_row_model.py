from typing import Protocol

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable, TRowModel

class IRowModel(IFeature[TRowModel], Protocol):
    pass


class RowModel(IRowModel[TRowModel], FeatureBase[TRowModel]):

    @staticmethod
    def init(table: ITable[TRowModel], updater:Updater[TRowModel]) -> IRowModel[TRowModel]:
        raise NotImplementedError()
