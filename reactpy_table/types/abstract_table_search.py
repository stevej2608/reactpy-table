from abc import abstractmethod
from .feature import Feature
from .abstract_table import Table


class TableSearch(Feature):

    @staticmethod
    def init(table: Table) -> 'TableSearch':
        raise NotImplementedError()

    @abstractmethod
    def table_search(self, text:str): ...
