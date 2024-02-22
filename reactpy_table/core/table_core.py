from copy import deepcopy
from typing import Callable, Any, Union, Type, Protocol
from pydantic import BaseModel
from reactpy import use_state
from utils.logger import log

from ..types import IColumnSort, ColumnSort, IPaginator, Paginator, ITableSearch, TableSearch, IRowModel, RowModel, ITable, TableData, TRowModel, Updater
from ..features import DefaultColumnSort, DefaultTableSearch, DefaultRowModel, DefaultPaginator

class IFeatureSet[TRowModel](Protocol):
    paginator: IPaginator[TRowModel]
    sort: IColumnSort[TRowModel]
    search: ITableSearch[TRowModel]
    row_model: IRowModel[TRowModel]

class Features[TRowModel](BaseModel):
    paginator: Type[Paginator[TRowModel]]
    sort: Type[ColumnSort[TRowModel]]
    search: Type[TableSearch[TRowModel]]
    row_model: Type[RowModel[TRowModel]]


class Table(ITable[TRowModel], IFeatureSet[TRowModel], Protocol):
    pass

class ReactpyTable[TRowModel](Table[TRowModel]):

    def __init__(self, data: TableData[TRowModel], updater: Updater[TRowModel], features: Features[TRowModel]):
        self.data = data
        self.paginator = features.paginator.init(self, updater=updater)
        self.sort = features.sort.init(self, updater=updater)
        self.search = features.search.init(self, updater=updater)
        self.row_model = features.row_model.init(self, updater=updater)


type TFeature[T] = Type[T] | None

class Options[TRowModel](TableData[TRowModel]):
    paginator: TFeature[Paginator[TRowModel]] = None
    sort: TFeature[ColumnSort[TRowModel]] = None
    search: TFeature[TableSearch[TRowModel]] = None


def use_reactpy_table[TRowModel](options: Options[TRowModel] = Options[TRowModel]()) -> ReactpyTable[TRowModel]:

    log.info('use_reactpy_table')

    set_table: Union[Callable[[Union[Any, Callable[[Any], Any]]], None], None]  = None

    def _create_table() -> ReactpyTable[TRowModel]:

        def state_updater(self: ITable[TRowModel]) -> None:
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
