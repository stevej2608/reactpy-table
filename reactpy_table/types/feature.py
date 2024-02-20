from typing import Callable, TypeVar, Any, cast
from ..types.abstract_table import Table

class Feature:
    table: Table

    @staticmethod
    def init(table: Table) -> 'Feature':
        raise NotImplementedError()

    @property
    def data(self):
        return self.table.data

    @property
    def initial_values(self):
        return self.table.data.cols


    def __init__(self, table:Table):
        self.table = table


    def updater(self) -> None:
        self.table.updater(self)


Func = TypeVar("Func", bound=Callable[..., Any])

def update_state(func: Func) -> Func:

    def wrapper(self: Feature, *args: Any, **kwargs: Any) -> Any:
        result = func(self, *args, **kwargs)
        self.updater()
        return result

    return cast(Func, wrapper)
