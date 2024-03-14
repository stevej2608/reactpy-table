from typing import Callable

from .abstract_table import ITable
from .table_data import TData

# Updater = Callable[..., None]


Updater = Callable[[ITable[TData]], None]
