from typing import Protocol


from .feature import IFeature, Updater
from .abstract_table import ITable

class IRowModel(IFeature, Protocol):

    @staticmethod
    def init(table: ITable, updater:Updater) -> 'IRowModel':
        raise NotImplementedError()
