from typing import Callable, Any, Union, Type
from reactpy import use_state
from utils.logger import log

from reactpy_table import DefaultColumnSort, DefaultTableSearch, DefaultRowModel, DefaultPaginator

from ..types.table_data import TableData
from ..types.abstract_table import Table

from ..types.abstract_paginator import Paginator
from ..types.abstract_column_sort import ColumnSort
from ..types.abstract_table_search import TableSearch
from ..types.feature import Feature


class ReactpyTable(Table):
    ...


type TypeFeature[T] = Type[T] | None

class Options(TableData):
    paginator: TypeFeature[Paginator] = None
    sort: TypeFeature[ColumnSort] = None
    search: TypeFeature[TableSearch] = None


def use_reactpy_table(options: Options = Options()) -> ReactpyTable:

    log.info('use_reactpy_table')

    set_table: Union[Callable[[Union[Any, Callable[[Any], Any]]], None], None]  = None

    def _create_table() -> ReactpyTable:
        table_data = TableData(rows=options.rows, cols=options.cols)
        table = ReactpyTable(
            data=table_data,
            paginator = options.paginator or DefaultPaginator,
            sort = options.sort or DefaultColumnSort,
            search = options.search or DefaultTableSearch,
            row_model = DefaultRowModel,
            )

        def state_updater(self: ReactpyTable, feature: Feature) -> None:
            log.info('Update table')
            try:
                assert set_table is not None
                set_table(self)
            except Exception as ex:
                log.info('Update model failed %s', ex)

        # table.updater = state_updater
        setattr(table, 'updater', state_updater)

        return table

    table, set_table = use_state(_create_table)

    return table
