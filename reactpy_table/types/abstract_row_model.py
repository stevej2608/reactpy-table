from typing import Protocol

from .abstract_table import TData
from .feature import FeatureBase, IFeature


class IRowModel(IFeature[TData], Protocol):
    pass


class RowModel(IRowModel[TData], FeatureBase[TData]):
    pass
