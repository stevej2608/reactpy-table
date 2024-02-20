from abc import abstractmethod
from .feature import Feature
from .table_data import Column
from .abstract_table import Table

class ColumnSort(Feature):

    @staticmethod
    def init(table: Table) -> 'ColumnSort':
        raise NotImplementedError()


    @abstractmethod
    def toggle_sort(self, col:Column) -> bool: ...

    @abstractmethod
    def is_sort_reverse(self, col:Column) -> bool: ...
