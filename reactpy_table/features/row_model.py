from ..types import IRowModel, Updater, ITable
from .feature_base import FeatureBase


class DefaultRowModel(IRowModel, FeatureBase):

    @staticmethod
    def init(table: ITable, updater:Updater) -> IRowModel:
        return DefaultRowModel(table=table, updater=updater)
