from typing import Callable

from .abstract_table import TableData
from .table_data import TData


# Updater = Callable[[ITable[TData]], None]
UpstreamData = Callable[[], TableData[TData]]
