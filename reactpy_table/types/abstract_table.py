from typing import Protocol
from .table_data import TableData

class ITable(Protocol):
    data: TableData
