from typing import Generic

from ..types import TableData, TData, Updater
from .feature_factories import FeatureFactories
from .table import Table


class ReactpyTable(Table[TData], Generic[TData]):

    @property
    def data(self) -> TableData[TData]:
        return self._data


    def __init__(self, data: TableData[TData], updater: Updater[TData], features: FeatureFactories[TData]):
        self._data = data
        self.paginator = features.paginator(self, updater)
        self.sort = features.sort(self, updater)
        self.search = features.search(self, updater)
        self.row_model = features.row_model(self, updater)
