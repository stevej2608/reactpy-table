from typing import Any, Callable, Union
from copy import copy
from reactpy import use_state

from utils.logger import log

from ..features import getDefaultColumnSort, getDefaultPaginator, getDefaultRowModel, getDefaultTableSearch
from ..types import TableData, TData

from .feature_factories import FeatureFactories
from .options import Options
from .reactpy_table import ReactpyTable
from .table import Table


def use_reactpy_table(options: Options[TData]) -> Table[TData]:
    log.info("use_reactpy_table")

    set_table: Union[Callable[[Union[Any, Callable[[Any], Any]]], None], None] = None

    def _create_table() -> Table[TData]:

        def state_updater(self: ReactpyTable[TData]) -> None:
            log.info("Update table")
            try:
                if set_table is not None:
                    set_table(copy(self))
            except Exception as ex:
                log.info("Update model failed %s", ex)

        table_data = TableData(rows=options.rows, cols=options.cols)

        table = ReactpyTable(
            data=table_data,
            updater=state_updater,
            features=FeatureFactories[TData](
                paginator=options.paginator or getDefaultPaginator(),
                sort=options.sort or getDefaultColumnSort(),
                search=options.search or getDefaultTableSearch(),
                row_model=options.row_model or getDefaultRowModel(),
            ),
        )

        # setattr(table, "updater", state_updater)

        return table.refresh()

    table, set_table = use_state(_create_table)

    return table
