from copy import deepcopy
from typing import Callable, Any, Union, Type, Protocol
from pydantic import BaseModel
from reactpy import use_state
from utils.logger import log

from ..types import IColumnSort, ColumnSort, IPaginator, Paginator, ITableSearch, TableSearch, IRowModel, RowModel, ITable, TableData, TData, Updater
from ..features import DefaultColumnSort, DefaultTableSearch, DefaultRowModel, DefaultPaginator

class IFeatureSet[TData](Protocol):
    paginator: IPaginator[TData]
    sort: IColumnSort[TData]
    search: ITableSearch[TData]
    row_model: IRowModel[TData]

class Features[TData](BaseModel):
    paginator: Type[Paginator[TData]]
    sort: Type[ColumnSort[TData]]
    search: Type[TableSearch[TData]]
    row_model: Type[RowModel[TData]]


class Table(ITable[TData], IFeatureSet[TData], Protocol):
    pass

class ReactpyTable[TData](Table[TData]):

    def __init__(self, data: TableData[TData], updater: Updater[TData], features: Features[TData]):
        self.data = data
        self.paginator = features.paginator.init(self, updater=updater)
        self.sort = features.sort.init(self, updater=updater)
        self.search = features.search.init(self, updater=updater)
        self.row_model = features.row_model.init(self, updater=updater)


type TFeature[T] = Type[T] | None

class Options[TData](TableData[TData]):
    paginator: TFeature[Paginator[TData]] = None
    sort: TFeature[ColumnSort[TData]] = None
    search: TFeature[TableSearch[TData]] = None


def use_reactpy_table[TData](options: Options[TData] = Options[TData]()) -> ReactpyTable[TData]:

    log.info('use_reactpy_table')

    set_table: Union[Callable[[Union[Any, Callable[[Any], Any]]], None], None]  = None

    def _create_table() -> ReactpyTable[TData]:

        def state_updater(self: ITable[TData]) -> None:
            log.info('Update table')
            try:
                assert set_table is not None
                set_table(deepcopy(self))
            except Exception as ex:
                log.info('Update model failed %s', ex)

        table_data = TableData(rows=options.rows, cols=options.cols)

        table = ReactpyTable(
            data=table_data,
            updater = state_updater,
            features = Features(
                paginator = options.paginator or DefaultPaginator,
                sort = options.sort or DefaultColumnSort,
                search = options.search or DefaultTableSearch,
                row_model = DefaultRowModel
                )
            )


        # table.updater = state_updater
        setattr(table, 'updater', state_updater)

        return table

    table, set_table = use_state(_create_table)

    return table
