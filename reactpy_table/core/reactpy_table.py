from typing import Generic, Self

from ..types import TableData, TData, Updater, ITable
from .feature_factories import FeatureFactories
from .table import Table


class ReactpyTable(Table[TData], Generic[TData]):

    @property
    def data(self) -> TableData[TData]:
        return self._data

    def _row_model_update(self):
        self._data = self.row_model.pipeline(self._data)
        self.model_update(self)

    def _paginator_update(self):
        self._data = self.paginator.pipeline(self._data)
        self._row_model_update()

    def _sort_update(self):
        self._data = self.sort.pipeline(self._data)
        self._paginator_update()

    def _search_update(self):
        self._data = self.search.pipeline(self._data)
        self._sort_update()

    def refresh(self) -> Self:
        self._search_update()
        return self

    def __init__(self, data: TableData[TData], updater: Updater[TData], features: FeatureFactories[TData]):

        def row_model_update(table: ITable[TData]):
            self._row_model_update()

        def paginator_update(table: ITable[TData]):
            self._paginator_update()

        def sort_update(table: ITable[TData]):
            self._sort_update()

        def search_update(table: ITable[TData]):
            self._search_update()


        self._data = data
        self.model_update = updater
        self.paginator = features.paginator(self, paginator_update)
        self.sort = features.sort(self, sort_update)
        self.search = features.search(self, search_update)
        self.row_model = features.row_model(self, row_model_update)
