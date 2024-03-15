from typing import Any, Callable, Generic, List, Protocol, TypeVar, cast

from .abstract_table import ITable
from .table_data import TableData, TData
from .updater import UpstreamData


class IFeature(Protocol, Generic[TData]):

    @property
    def data(self) -> TableData[TData]:
        ...

    @property
    def initial_values(self) -> List[TData]:
        ...

    pipeline: Callable[[], TableData[TData]]


class FeatureBase(IFeature[TData], Generic[TData]):
    table: ITable[TData]
    # updater: UpstreamData[TData]

    _initial_values: List[TData]

    @property
    def data(self) -> TableData[TData]:
        return self.table.data

    @property
    def initial_values(self) -> List[TData]:
        return self._initial_values


    # def pipeline(self, table_data:TableData[TData]) -> TableData[TData]:
    #     """Data processing pipeline

    #     Args:
    #         table_data (TableData[TData]): Upstream data to be processed

    #     Returns:
    #         TableData[TData]: processed result
    #     """
    #     ... # pylint: disable=unnecessary-ellipsis

    def __init__(self, table: ITable[TData], upstream_data: UpstreamData[TData]):
        self.table = table
        # self.updater = upstream_data
        self._initial_values = table.data.rows

        # self._pipeline_data: TableData[TData] = TableData(rows=[], cols=[])


TFeature= TypeVar("TFeature")
TFeatureFactory = Callable[[ITable[TData], UpstreamData[TData]], TFeature]
"""Generic signature of a Callable that returns a Feature instance

Returns:
    TFeature: When called returns an instantiated feature

Example Usage:
```
def getMyRowModel(<custom parameters>) -> TFeatureFactory[TData, RowModel[TData]]:

    # < Any persistent data/refs here>

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> RowModel[TData]:
    
        # <Any pre-initialization code here>

        return MyRowModel(table=table, updater=updater, <Any Additional Args>)

    return wrapper
```
"""

Func = TypeVar("Func", bound=Callable[..., Any])
def update_state(func: Func) -> Func:
    def wrapper(self: FeatureBase[TData], *args: Any, **kwargs: Any) -> Any:
        result = func(self, *args, **kwargs)
        self.table.refresh()
        return result

    return cast(Func, wrapper)
