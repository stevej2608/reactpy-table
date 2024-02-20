from .feature import Feature
from .abstract_table import Table

class RowModel(Feature):

    @staticmethod
    def init(table: Table) -> 'RowModel':
        raise NotImplementedError()
