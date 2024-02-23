from typing import Protocol, Generic
from .table_data import TableData, TData

class ITable(Protocol, Generic[TData]):
    data: TableData[TData]
