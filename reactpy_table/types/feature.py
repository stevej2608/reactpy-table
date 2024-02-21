from typing import Protocol, Callable
from .table_data import TableData
from .abstract_table import ITable

Updater = Callable[[ITable], None]

class IFeature(Protocol) :

    @staticmethod
    def init(table: ITable, updater: Updater) -> 'IFeature': ...

    @property
    def data(self) -> TableData: ...

    @property
    def initial_values(self) -> TableData: ...
