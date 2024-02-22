from typing import Protocol, Callable, TypeVar, Any, cast, List
from .table_data import TableData, RowData, TRowModel
from .abstract_table import ITable

type Updater[TRowModel] = Callable[[ITable[TRowModel]], None]

class IFeature[TRowModel](Protocol) :

    @staticmethod
    def init(table: ITable[TRowModel], updater: Updater[TRowModel]) -> 'IFeature[TRowModel]': ...

    @property
    def data(self) -> TableData[TRowModel]: ...

    @property
    def initial_values(self) -> List[RowData]: ...


class FeatureBase[TRowModel](IFeature[TRowModel]):

    table: ITable[TRowModel]
    updater: Updater[TRowModel]

    _initial_values: List[RowData]

    @property
    def data(self) -> TableData[TRowModel]:
        return self.table.data

    @property
    def initial_values(self) -> List[RowData]:
        return self._initial_values

    def __init__(self,table: ITable[TRowModel], updater: Updater[TRowModel]):
        self.table = table
        self.updater = updater
        self._initial_values = table.data.rows


Func = TypeVar("Func", bound=Callable[..., Any])

def update_state(func: Func) -> Func:

    def wrapper(self: FeatureBase[TRowModel], *args: Any, **kwargs: Any) -> Any:
        result = func(self, *args, **kwargs)
        self.updater(self.table)
        return result

    return cast(Func, wrapper)
