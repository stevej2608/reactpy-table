from typing import Protocol

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable

class IRowModel(IFeature, Protocol):
    pass


class RowModel(IRowModel, FeatureBase):

    @staticmethod
    def init(table: ITable, updater:Updater) -> IRowModel:
        raise NotImplementedError()
