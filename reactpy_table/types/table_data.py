from typing import List, Any, Callable, Optional, TypeVar, Generic
from pydantic import BaseModel


Updater = Callable[[], None]

RowData = BaseModel | Any

class Column(BaseModel):
    name: str
    label: str
    style: Optional[str] = None
    sort : Optional[Callable[['Column'], None]] = None
    width: str = ""


Columns = List[Column]

# class TableData(BaseModel):
#     rows: List[RowData] = []
#     cols: Columns = []


TData = TypeVar('TData', bound=RowData)

class TableData(BaseModel, Generic[TData]):
    rows: List[TData] = []
    cols: Columns = []
