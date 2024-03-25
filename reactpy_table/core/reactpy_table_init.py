from typing import Any, Callable, Union
from copy import copy
from reactpy import use_state, use_memo

from utils import log

from ..features import getDefaultColumnSort, getDefaultPaginator, getDefaultRowModel, getDefaultTableSearch
from ..types import TableData, TData

from .feature_factories import FeatureFactories
from .core_options import CoreTableOptions
from .options import Options
from .reactpy_table import ReactpyTable
from .table import Table


def use_reactpy_table(options: Options[TData]) -> Table[TData]:

    set_refresh: Callable[[int], None] | None = None

    core_options = use_memo(lambda: CoreTableOptions(options), [options])
    table_data = use_memo(lambda: TableData(rows=options.rows, cols=options.cols), [options.rows, options.cols])

    def _create_table() -> Table[TData]:

        def state_updater(table: ReactpyTable[TData]) -> None:
            if set_refresh:
                set_refresh(table.UID)

        table = ReactpyTable(
            data=table_data,
            updater=state_updater,
            table_options = core_options,
            features=FeatureFactories[TData](
                paginator=options.paginator or getDefaultPaginator(),
                sort=options.sort or getDefaultColumnSort(),
                search=options.search or getDefaultTableSearch(),
                row_model=options.row_model or getDefaultRowModel(),
            ),
        )

        log.info('Created table id=%s', id(table))

        return table.refresh()

    table, _ = use_state(_create_table)

    _, set_refresh = use_state(table.UID)

    log.info('table=%s', id(table))

    if core_options != table.table_options:
        table.set_options(core_options)

    if table_data != table.initial_data:
        table.set_table_data(table_data)


    return table
