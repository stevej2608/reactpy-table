from typing import List, Callable, Optional, TypeVar, Generic, Protocol, Dict, Any
from pydantic import BaseModel


class IBaseModel(Protocol):
    '''By default the row data supplied by the user will be derived from
    the pydantic BaseModel class. Other row data types will need to 
    implement IBaseModel protocol    
    '''

    def model_dump(self) -> Dict[str, Any]: ...

RowData = BaseModel | IBaseModel

class Column(BaseModel):
    """Column definitions"""
    name: str
    label: str
    style: Optional[str] = None
    sort : Optional[Callable[['Column'], None]] = None
    width: str = ""

Columns = List[Column]


TData = TypeVar('TData', bound=RowData)

class TableData(Generic[TData]):
    rows: List[TData] = []
    cols: Columns = []

    def __init__(self, rows:List[TData], cols: Columns):
        self.rows = rows
        self.cols = cols
