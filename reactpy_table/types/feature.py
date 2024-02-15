from typing import Callable, TypeVar, Any, cast

from pydantic import BaseModel
from .table_data import TableData, Updater


class Feature(BaseModel):
    data: TableData
    updater: Updater

Func = TypeVar("Func", bound=Callable[..., Any])

def update_state(func: Func) -> Func:

    def wrapper(self: Feature, *args: Any, **kwargs: Any) -> Any:
        result = func(self, *args, **kwargs)
        self.updater()
        return result

    return cast(Func, wrapper)
