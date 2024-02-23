from typing import Protocol

from .feature import IFeature, FeatureBase
from .abstract_table import TData


class IRowModel(IFeature[TData], Protocol):
    pass


class RowModel(IRowModel[TData], FeatureBase[TData]):
    pass
