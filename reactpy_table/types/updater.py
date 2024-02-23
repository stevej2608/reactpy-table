from typing import Callable
from .table_data import TData
from .abstract_table import ITable

Updater = Callable[[ITable[TData]], None]
