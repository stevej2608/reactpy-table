from typing import Protocol, Callable, TypeVar, Any, cast, List
from .table_data import TableData, RowData, TData
from .abstract_table import ITable

type Updater[TData] = Callable[[ITable[TData]], None]

class IFeature[TData](Protocol) :

    @staticmethod
    def init(table: ITable[TData], updater: Updater[TData]) -> 'IFeature[TData]': ...

    @property
    def data(self) -> TableData[TData]: ...

    @property
    def initial_values(self) -> List[RowData]: ...


class FeatureBase[TData](IFeature[TData]):

    table: ITable[TData]
    updater: Updater[TData]

    _initial_values: List[RowData]

    @property
    def data(self) -> TableData[TData]:
        return self.table.data

    @property
    def initial_values(self) -> List[RowData]:
        return self._initial_values

    def __init__(self,table: ITable[TData], updater: Updater[TData]):
        self.table = table
        self.updater = updater
        self._initial_values = table.data.rows


Func = TypeVar("Func", bound=Callable[..., Any])

def update_state(func: Func) -> Func:

    def wrapper(self: FeatureBase[TData], *args: Any, **kwargs: Any) -> Any:
        result = func(self, *args, **kwargs)
        self.updater(self.table)
        return result

    return cast(Func, wrapper)
