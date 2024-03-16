from typing import Any, Callable, Generic, List, Protocol, TypeVar, cast

from .abstract_table import ITable
from .table_data import TableData, TData
from .updater import UpstreamData


class IFeature(Protocol, Generic[TData]):

    @property
    def data(self) -> TableData[TData]:
        ...

    pipeline: Callable[[], TableData[TData]]


class FeatureBase(IFeature[TData], Generic[TData]):
    table: ITable[TData]
    # updater: UpstreamData[TData]

    _initial_values: List[TData]

    @property
    def data(self) -> TableData[TData]:
        return self._table.data

    @property
    def table(self) -> ITable[TData]:
        return self._table

    def __init__(self, table: ITable[TData], upstream_data: UpstreamData[TData]):
        self._table = table


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
