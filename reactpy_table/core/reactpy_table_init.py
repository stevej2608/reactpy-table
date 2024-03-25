from typing import Callable
from reactpy import use_state, use_memo

from utils import log

from ..features import getDefaultColumnSort, getDefaultPaginator, getDefaultRowModel, getDefaultTableSearch
from ..types import TData

from .feature_factories import FeatureFactories
from .core_options import TableState
from .options import Options
from .reactpy_table import ReactpyTable
from .table import Table


def use_reactpy_table(options: Options[TData]) -> Table[TData]:


    core_options = use_memo(lambda: TableState(options), [options])
    # table_data = use_memo(lambda: TableData(rows=options.rows, cols=options.cols), [options.rows, options.cols])

    def create_table() -> Table[TData]:

        set_refresh: Callable[[int], None] | None = None

        def state_updater(table: ReactpyTable[TData]) -> None:
            if set_refresh:
                set_refresh(table.UID)

        def _create_table() -> Table[TData]:
            table =  ReactpyTable(
                updater=state_updater,
                table_options = core_options,
                features=FeatureFactories[TData](
                    paginator=options.paginator or getDefaultPaginator(),
                    sort=options.sort or getDefaultColumnSort(),
                    search=options.search or getDefaultTableSearch(),
                    row_model=options.row_model or getDefaultRowModel(),
                ),
            )

            return table.refresh()

        table, _ = use_state(_create_table)
        _, set_refresh = use_state(table.UID)

        return table


    table = create_table()

    log.info('table=%s', id(table))

    if core_options != table.table_state:
        table.set_options(core_options)



    return table
