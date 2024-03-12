from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Callable, Generic, Union

from reactpy import use_state
from utils.logger import log

from ..features import getDefaultColumnSort, getDefaultPaginator, getDefaultRowModel, getDefaultTableSearch
from ..types import ColumnSort, ITable, Paginator, RowModel, TableData, TableSearch, TData, TFeatureFactory, Updater
from .options import Options
from .table import Table


@dataclass
class _FeatureFactories(Generic[TData]):
    paginator: TFeatureFactory[TData, Paginator[TData]]
    sort: TFeatureFactory[TData, ColumnSort[TData]]
    search: TFeatureFactory[TData, TableSearch[TData]]
    row_model: TFeatureFactory[TData, RowModel[TData]]


class _ReactpyTable(Table[TData], Generic[TData]):
    def __init__(self, data: TableData[TData], updater: Updater[TData], features: _FeatureFactories[TData]):
        self.data = data
        self.paginator = features.paginator(self, updater)
        self.sort = features.sort(self, updater)
        self.search = features.search(self, updater)
        self.row_model = features.row_model(self, updater)


def use_reactpy_table(options: Options[TData]) -> Table[TData]:
    log.info("use_reactpy_table")

    set_table: Union[Callable[[Union[Any, Callable[[Any], Any]]], None], None] = None

    def _create_table() -> Table[TData]:

        def state_updater(self: ITable[TData]) -> None:
            log.info("Update table")
            try:
                assert set_table is not None
                set_table(deepcopy(self))
            except Exception as ex:
                log.info("Update model failed %s", ex)

        table_data = TableData(rows=options.rows, cols=options.cols)

        table = _ReactpyTable(
            data=table_data,
            updater=state_updater,
            features=_FeatureFactories[TData](
                paginator=options.paginator or getDefaultPaginator(),
                sort=options.sort or getDefaultColumnSort(),
                search=options.search or getDefaultTableSearch(),
                row_model=options.row_model or getDefaultRowModel(),
            ),
        )

        setattr(table, "updater", state_updater)
        return table

    table, set_table = use_state(_create_table)

    return table
