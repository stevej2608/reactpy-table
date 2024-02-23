from copy import deepcopy
from dataclasses import dataclass
from typing import Callable, Any, Union, Type, Protocol, Generic, List
from reactpy import use_state
from utils.logger import log

from ..types import IColumnSort, IPaginator,IRowModel, ITable, ITableSearch
from ..types import Columns, ColumnSort, Paginator, RowModel, TableData, TableSearch, TData, Updater

from ..features import DefaultColumnSort, DefaultTableSearch, DefaultRowModel, DefaultPaginator

class IFeatureSet(Protocol, Generic[TData]):
    paginator: IPaginator[TData]
    sort: IColumnSort[TData]
    search: ITableSearch[TData]
    row_model: IRowModel[TData]

@dataclass
class Features(Generic[TData]):
    paginator: Type[Paginator[TData]]
    sort: Type[ColumnSort[TData]]
    search: Type[TableSearch[TData]]
    row_model: Type[RowModel[TData]]


class Table(ITable[TData], IFeatureSet[TData], Protocol):
    pass

class ReactpyTable(Table[TData], Generic[TData]):

    def __init__(self, data: TableData[TData], updater: Updater[TData], features: Features[TData]):
        self.data = data
        self.paginator = features.paginator.init(self, updater=updater)
        self.sort = features.sort.init(self, updater=updater)
        self.search = features.search.init(self, updater=updater)
        self.row_model = features.row_model.init(self, updater=updater)


type FeatureType[T] = Type[T] | None

class Options(TableData[TData], Generic[TData]):

    paginator: FeatureType[Paginator[TData]] = None
    sort: FeatureType[ColumnSort[TData]] = None
    search: FeatureType[TableSearch[TData]] = None

    def __init__(self,
            rows: List[TData],
            cols: Columns,
            paginator: FeatureType[Paginator[TData]] = None,
            sort: FeatureType[ColumnSort[TData]] = None,
            search: FeatureType[TableSearch[TData]] = None
            ):

        super().__init__(rows=rows, cols=cols)

        self.paginator = paginator
        self.sort = sort
        self.search = search


def use_reactpy_table(options: Options[TData]) -> ReactpyTable[TData]:

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
            features = Features[TData](
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
