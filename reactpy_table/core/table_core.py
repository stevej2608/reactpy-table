from typing import Callable, Any, Union, Type, Protocol
from pydantic import BaseModel

from reactpy import use_state
from utils.logger import log

from ..types import IColumnSort, ColumnSort, IPaginator, Paginator, ITableSearch, TableSearch, IRowModel, RowModel, ITable, TableData, Updater
from ..features import DefaultColumnSort, DefaultTableSearch, DefaultRowModel, DefaultPaginator

class IFeatureSet(Protocol):
    paginator: IPaginator
    sort: IColumnSort
    search: ITableSearch
    row_model: IRowModel

class Features(BaseModel):
    paginator: Type[Paginator]
    sort: Type[ColumnSort]
    search: Type[TableSearch]
    row_model: Type[RowModel]


class Table(ITable, IFeatureSet, Protocol):
    pass

class ReactpyTable(Table):

    def __init__(self, data: TableData, updater: Updater, features: Features):
        self.data = data
        self.paginator = features.paginator.init(self, updater=updater)
        self.sort = features.sort.init(self, updater=updater)
        self.search = features.search.init(self, updater=updater)
        self.row_model = features.row_model.init(self, updater=updater)


type TFeature[T] = Type[T] | None

class Options(TableData):
    paginator: TFeature[Paginator] = None
    sort: TFeature[ColumnSort] = None
    search: TFeature[TableSearch] = None


def use_reactpy_table(options: Options = Options()) -> ReactpyTable:

    log.info('use_reactpy_table')

    set_table: Union[Callable[[Union[Any, Callable[[Any], Any]]], None], None]  = None

    def _create_table() -> ReactpyTable:

        def state_updater(self: ITable) -> None:
            log.info('Update table')
            try:
                assert set_table is not None
                set_table(self)
            except Exception as ex:
                log.info('Update model failed %s', ex)

        table_data = TableData(rows=options.rows, cols=options.cols)

        table = ReactpyTable(
            data=table_data,
            updater = state_updater,
            features = Features(
                paginator = DefaultPaginator,
                sort = DefaultColumnSort,
                search = DefaultTableSearch,
                row_model = DefaultRowModel
                )
            )


        # table.updater = state_updater
        setattr(table, 'updater', state_updater)

        return table

    table, set_table = use_state(_create_table)

    return table
