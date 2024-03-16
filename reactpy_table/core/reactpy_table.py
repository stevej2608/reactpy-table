from typing import Generic, Self, Callable

from utils import log

from ..types import TableData, TData
from .feature_factories import FeatureFactories
from .table import Table


class ReactpyTable(Table[TData], Generic[TData]):

    @property
    def data(self) -> TableData[TData]:
        return self._data

    def refresh(self) -> Self:

        log.info('refresh - start')

        # The following call triggers an update of
        # the entire feature pipeline

        self._data = self.row_model.pipeline()
        self.model_update(self)

        log.info('refresh - end')

        return self


    def __init__(self, data: TableData[TData],
                 updater: Callable[['ReactpyTable[TData]'], None],
                 features: FeatureFactories[TData]):

        # Daisy chain the feature pipeline. Each of
        # these functions is passed into it's respective
        # feature. Each function returns the table data
        # from the next feature up the pipeline.

        def search_update() -> TableData[TData]:
            return self._initial_data

        def sort_update() -> TableData[TData]:
            return self.search.pipeline()

        def paginator_update() -> TableData[TData]:
            return self.sort.pipeline()

        def row_model_update() -> TableData[TData]:
            return self.paginator.pipeline()

        log.info('<<<<<<<<<<<<<<<< ReactpyTable.__init__, rows=%s >>>>>>>>>>>>>>>>> ', len(data.rows))

        self._initial_data: TableData[TData] = data
        self._data: TableData[TData] = data
        self.model_update = updater
        self.search = features.search(self, search_update)
        self.sort = features.sort(self, sort_update)
        self.paginator = features.paginator(self, paginator_update)
        self.row_model = features.row_model(self, row_model_update)
