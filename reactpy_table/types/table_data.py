from typing import List, Any, Callable, Optional
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

class TableData(BaseModel):
    rows: List[RowData] = []
    cols: Columns = []


# TBaseModel = TypeVar('TBaseModel', bound=BaseModel)

# class Table(BaseModel, Generic[TBaseModel]):
#     rows: List[TBaseModel]

# class TableData(BaseModel, Generic[TBaseModel]):
#     rows: List[TBaseModel] = []
#     cols: Columns = []
