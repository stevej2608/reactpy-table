from abc import abstractmethod
from .feature import Feature
from .table_data import Column

class ColumnSort(Feature):

    @abstractmethod
    def toggle_sort(self, col:Column) -> bool: ...

    @abstractmethod
    def is_sort_reverse(self, col:Column) -> bool: ...
