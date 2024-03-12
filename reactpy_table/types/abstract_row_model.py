from typing import Protocol

from .abstract_table import TData
from .feature import FeatureBase, IFeature


class IRowModel(IFeature[TData], Protocol):

    def delete_row(self, index:int) -> None:
        """Delete the given row"""

    def update_row(self, index:int, row:TData) -> None:
        """Update the given row"""

class RowModel(IRowModel[TData], FeatureBase[TData]):
    pass
