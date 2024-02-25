from typing import Protocol, Callable, TypeVar, Any, cast, List, Generic
from .table_data import TableData, TData
from .abstract_table import ITable
from .updater import Updater


class IFeature(Protocol, Generic[TData]):

    @property
    def data(self) -> TableData[TData]:
        ...

    @property
    def initial_values(self) -> List[TData]:
        ...


class FeatureBase(IFeature[TData], Generic[TData]):
    table: ITable[TData]
    updater: Updater[TData]

    _initial_values: List[TData]

    @property
    def data(self) -> TableData[TData]:
        return self.table.data

    @property
    def initial_values(self) -> List[TData]:
        return self._initial_values

    def __init__(self, table: ITable[TData], updater: Updater[TData]):
        self.table = table
        self.updater = updater
        self._initial_values = table.data.rows


TFeature= TypeVar("TFeature")
TFeatureFactory = Callable[[ITable[TData], Updater[TData]], TFeature]
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
        self.updater(self.table)
        return result

    return cast(Func, wrapper)
