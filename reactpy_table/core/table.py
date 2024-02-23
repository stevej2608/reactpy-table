from typing import Protocol

from ..types import ITable, TData

from .feature_set import IFeatureSet

class Table(ITable[TData], IFeatureSet[TData], Protocol):
    pass
