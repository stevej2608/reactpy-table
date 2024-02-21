from typing import Callable, TypeVar, Any, cast
from ..types import ITable, Updater, TableData, IFeature

class FeatureBase(IFeature):

    table: ITable
    updater: Updater

    @property
    def data(self) -> TableData:
        return self.table.data

    @property
    def initial_values(self) -> TableData:
        return self.table.data


    def __init__(self, table:ITable, updater: Updater):
        self.table = table
        self.updater = updater


Func = TypeVar("Func", bound=Callable[..., Any])

def update_state(func: Func) -> Func:

    def wrapper(self: FeatureBase, *args: Any, **kwargs: Any) -> Any:
        result = func(self, *args, **kwargs)
        self.updater(self.table)
        return result

    return cast(Func, wrapper)
