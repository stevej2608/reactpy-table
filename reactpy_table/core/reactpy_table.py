from typing import Generic, Self, Callable, Protocol, cast, Any, Generator
import random
from utils import log
from ..types import TableData, TData
from .feature_factories import FeatureFactories
from .table import Table

from .core_options import CoreTableOptions


def unique_id():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


class ReactpyTable(Table[TData], Generic[TData]):

    @property
    def data(self) -> TableData[TData]:
        return self._data
    
    @property
    def initial_data(self) -> TableData[TData]:
        return self._initial_data

    @property
    def table_options(self) -> CoreTableOptions:
        return self._table_options

    @property
    def UID(self) -> int:
        return next(self._unique_sequence)


    def refresh(self) -> Self:

        # The following call triggers an update of
        # the entire feature pipeline

        try:
            self._data = self.row_model.pipeline()

            log.info('refresh data=%s', str(self._data.rows[0])[0:50])

            # TODO: Why has this become a tuple???

            self._updater[0](self)


            return self
        except Exception as ex:
            log.info('Update failed %s', ex)

        return self


    def set_options(self, table_options: CoreTableOptions) -> None:
        self._table_options = table_options
        self.refresh()


    def set_table_data(self, data:TableData[TData]) -> None:
        self._initial_data = data
        log.info('_initial_data %s', str(self._initial_data.rows[0])[0:50])
        self.refresh()


    def __init__(self, data: TableData[TData],
                 updater: Callable[['ReactpyTable[TData]'], None],
                 table_options: CoreTableOptions,
                 features: FeatureFactories[TData]):

        # Daisy chain the feature pipeline. Each of
        # these functions is passed into it's respective
        # feature. Each function returns the table data
        # from the next feature up the pipeline.

        def search_update() -> TableData[TData]:
            log.info('          5. _initial_data %s...', str(self._initial_data.rows[0])[0:50])
            return self._initial_data

        def sort_update() -> TableData[TData]:
            return self.search.pipeline()

        def paginator_update() -> TableData[TData]:
            return self.sort.pipeline()

        def row_model_update() -> TableData[TData]:
            return self.paginator.pipeline()


        self._initial_data: TableData[TData] = data
        self._data: TableData[TData] = data
        self._updater = updater,
        self._table_options = table_options
        self._unique_sequence = unique_id()
        self.search = features.search(self, search_update)
        self.sort = features.sort(self, sort_update)
        self.paginator = features.paginator(self, paginator_update)
        self.row_model = features.row_model(self, row_model_update)
