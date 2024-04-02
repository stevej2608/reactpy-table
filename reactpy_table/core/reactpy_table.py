from typing import Generic, Self, Callable, cast
import random
from utils import log
from ..types import TableData, TData
from .feature_factories import FeatureFactories
from .table import Table

from ..types.table_state import TableState


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
    def table_state(self) -> TableState[TData]:
        return self._table_state

    @property
    def UID(self) -> int:
        return next(self._unique_sequence)


    def refresh_data_dump(self):
        if self._data.rows:
            return f"{str(self._data.rows[0])[0:50]} ..."
        else:
            return 'Empty'


    def refresh(self) -> Self:

        try:
            # The following call triggers an update of
            # the entire feature pipeline

            self._data = self.row_model.pipeline()

            # log.info('refresh data=%s', self.refresh_data_dump())

            self._updater(self)

            return self
        except Exception as ex:
            log.info('Update failed %s', ex)
            raise(ex)

        return self


    def set_options(self, table_options: TableState[TData], refresh:bool = True) -> None:

        data = TableData(rows = table_options.rows, cols=table_options.cols)

        self._initial_data: TableData[TData] = data
        self._data: TableData[TData] = data

        self._table_state = table_options

        if refresh:
            self.refresh()


    def __init__(self,
                 updater: Callable[['ReactpyTable[TData]'], None],
                 table_options: TableState[TData],
                 features: FeatureFactories[TData]):

        # Daisy chain the feature pipeline. Each of
        # these functions is passed into it's respective
        # feature. Each function returns the table data
        # from the next feature up the pipeline.

        def search_update() -> TableData[TData]:
            # if self._initial_data.rows:
            #     log.info('          5. _initial_data %s...', self.refresh_data_dump())
            return self._initial_data

        def sort_update() -> TableData[TData]:
            return self.search.pipeline()

        def paginator_update() -> TableData[TData]:
            return self.sort.pipeline()

        def row_model_update() -> TableData[TData]:
            return self.paginator.pipeline()


        self._initial_data = cast(TableData[TData], None)
        self._data = cast(TableData[TData], None)

        self.set_options(table_options=table_options, refresh=False)

        self._updater = updater
        self._table_state = table_options
        self._unique_sequence = unique_id()

        self.search = features.search(self, search_update)
        self.sort = features.sort(self, sort_update)
        self.paginator = features.paginator(self, paginator_update)
        self.row_model = features.row_model(self, row_model_update)
