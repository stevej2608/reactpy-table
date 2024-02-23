from copy import deepcopy
from typing import Callable, Any, Union, Generic
from reactpy import use_state
from utils.logger import log

from ..types import ITable, TableData, TData, Updater
from ..features import DefaultColumnSort, DefaultTableSearch, DefaultRowModel, DefaultPaginator

from .feature_set import Features
from .options import Options
from .table import Table


class _ReactpyTable(Table[TData], Generic[TData]):

    def __init__(self, data: TableData[TData], updater: Updater[TData], features: Features[TData]):
        self.data = data
        self.paginator = features.paginator.init(self, updater=updater)
        self.sort = features.sort.init(self, updater=updater)
        self.search = features.search.init(self, updater=updater)
        self.row_model = features.row_model.init(self, updater=updater)


def use_reactpy_table(options: Options[TData]) -> Table[TData]:

    log.info('use_reactpy_table')

    set_table: Union[Callable[[Union[Any, Callable[[Any], Any]]], None], None]  = None

    def _create_table() -> Table[TData]:

        def state_updater(self: ITable[TData]) -> None:
            log.info('Update table')
            try:
                assert set_table is not None
                set_table(deepcopy(self))
            except Exception as ex:
                log.info('Update model failed %s', ex)

        table_data = TableData(rows=options.rows, cols=options.cols)

        table = _ReactpyTable(
            data=table_data,
            updater = state_updater,
            features = Features[TData](
                paginator = options.paginator or DefaultPaginator,
                sort = options.sort or DefaultColumnSort,
                search = options.search or DefaultTableSearch,
                row_model = DefaultRowModel
                )
            )

        setattr(table, 'updater', state_updater)
        return table

    table, set_table = use_state(_create_table)

    return table
