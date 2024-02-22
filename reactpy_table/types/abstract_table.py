from typing import Protocol, Generic
from .table_data import TableData, TRowModel

class ITable(Protocol, Generic[TRowModel]):
    data: TableData[TRowModel]
