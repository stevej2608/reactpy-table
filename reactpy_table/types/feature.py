from typing import Protocol, Callable, TypeVar, Any, cast
from .table_data import TableData, RowData
from .abstract_table import ITable

Updater = Callable[[ITable], None]

class IFeature(Protocol) :

    @staticmethod
    def init(table: ITable, updater: Updater) -> 'IFeature': ...

    @property
    def data(self) -> TableData: ...

    @property
    def initial_values(self) -> RowData: ...


class FeatureBase(IFeature):

    table: ITable
    updater: Updater

    _initial_values: RowData

    @property
    def data(self) -> TableData:
        return self.table.data

    @property
    def initial_values(self) -> RowData:
        return self._initial_values

    def __init__(self,table: ITable, updater: Updater):
        self.table = table
        self.updater = updater
        self._initial_values = table.data.rows


Func = TypeVar("Func", bound=Callable[..., Any])

def update_state(func: Func) -> Func:

    def wrapper(self: FeatureBase, *args: Any, **kwargs: Any) -> Any:
        result = func(self, *args, **kwargs)
        self.updater(self.table)
        return result

    return cast(Func, wrapper)
