from typing import Any, Callable, Dict, Generic, List, Optional, Protocol, TypeVar

from pydantic import BaseModel

# https://tanstack.com/table/v8/docs/api/core/column-def

class ColumnDef(BaseModel):
    """Column definitions"""

    name: str
    label: str
    style: Optional[str] = None
    sort: Optional[Callable[["ColumnDef"], None]] = None
    width: str = ""


Columns = List[ColumnDef]


class IBaseModel(Protocol):
    """By default the row data supplied by the user will be derived from
    the pydantic BaseModel class. Other row data types will need to
    implement IBaseModel protocol
    """

    def model_dump(self) -> Dict[str, Any]:
        ...


TData = TypeVar("TData", bound=BaseModel | IBaseModel)


class TableData(Generic[TData]):
    rows: List[TData] = []
    cols: Columns = []

    def __init__(self, rows: List[TData], cols: Columns):
        self.rows = rows
        self.cols = cols
